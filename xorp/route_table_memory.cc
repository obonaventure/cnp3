#define DEBUG_LOGGING
#define DEBUG_PRINT_FUNCTION_NAME

#include "bgp_module.h"
#include "libxorp/xlog.h"
#include "route_table_memory.hh"
#include "route_table_deletion.hh"
#include "rib_ipc_handler.hh"
#include "bgp.hh"

template<class A>
MemoryTable<A>::MemoryTable(string table_name,
			  Safi safi, BGPRouteTable<A> *parent_table)
    : 	BGPRouteTable<A>("MemoryTable-" + table_name, safi)
{
    this->_parent = parent_table;
    _route_table = new RefTrie<A, MemorySubnetRoute<A> >;
    _genid = 1; /*zero is not a valid genid*/
    _table_version = 1;

}

template<class A>
MemoryTable<A>::~MemoryTable()
{
    delete _route_table;
}

template<class A>
void
MemoryTable<A>::flush()
{
    debug_msg("%s\n", this->tablename().c_str());
    _route_table->delete_all_nodes();
}

// - If add_route is called, it means that the route doesn't
//   exist upstream (otherwhise replace_route would have been called
// - But the route can still exist in this route table if a
//   delete_route for this route has been called has been called 
//   before for instance.

template<class A>
int
MemoryTable<A>::add_route(InternalMessage<A> &rtmsg,
			 BGPRouteTable<A> *caller)
{
    debug_msg("\n         %s\n caller: %s\n rtmsg: %p route: %p\n%s\n",
	      this->tablename().c_str(),
	      caller ? caller->tablename().c_str() : "NULL",
	      &rtmsg,
	      rtmsg.route(),
	      rtmsg.str().c_str());

    typedef ::AttributeMemory<A> AttributeMemory;
    
    XLOG_ASSERT(caller == this->_parent);
    XLOG_ASSERT(this->_next_table != NULL);
    const SubnetRoute<A> *existing_route=rtmsg.route();

    // Create the concise format PA list.
    PAListRef<A> pa_list = new PathAttributeList<A>(rtmsg.attributes());
    pa_list.register_with_attmgr();
    
    typename RefTrie<A, MemorySubnetRoute<A> >::iterator iter = _route_table->lookup_node(existing_route->net());
    
    // the route is still existing, update it's history

    if (iter != _route_table->end()) {
	MemorySubnetRoute<A> *trie_route = (MemorySubnetRoute<A> *) &(iter.payload());
	
	AttributeMemory *m= new AttributeMemory();
    	TimerList::system_gettimeofday(&m->when); 
    	m->_attributes = existing_route->attributes();
    	trie_route->history.push_front(m);
	
	if((int)trie_route->history.size() > MAX_HISTORY_SIZE)
		trie_route->history.pop_back();

    } else {
    // the route doesn't exist,  initiate its history
        MemorySubnetRoute<A>* tmp_route = new MemorySubnetRoute<A>(existing_route->net(), pa_list);
        
        AttributeMemory *m= new AttributeMemory();
        TimerList::system_gettimeofday(&m->when); 
        m->_attributes = existing_route->attributes(); 
        tmp_route->history.push_front(m);
	
        if((int)tmp_route->history.size() > MAX_HISTORY_SIZE)
       	    tmp_route->history.pop_back();

        _route_table->insert(existing_route->net(), *tmp_route);
        tmp_route->unref();
    }

    return this->_next_table->add_route(rtmsg, (BGPRouteTable<A>*)this);    
}

template<class A>
int
MemoryTable<A>::replace_route(InternalMessage<A> &old_rtmsg, 
			      InternalMessage<A> &new_rtmsg, 
			      BGPRouteTable<A> *caller)
{
    debug_msg("\n         %s\n"
	      "caller: %s\n"
	      "old rtmsg: %p new rtmsg: %p "
	      "old route: %p"
	      "new route: %p"
	      "old: %s\n new: %s\n",
	      this->tablename().c_str(),
	      caller->tablename().c_str(),
	      &old_rtmsg,
	      &new_rtmsg,
	      old_rtmsg.route(),
	      new_rtmsg.route(),
	      old_rtmsg.str().c_str(),
	      new_rtmsg.str().c_str());

    XLOG_ASSERT(caller == this->_parent);
    XLOG_ASSERT(this->_next_table != NULL);
    
    typedef ::AttributeMemory<A> AttributeMemory;
    const SubnetRoute<A> *existing_route=old_rtmsg.route();
    const SubnetRoute<A> *new_route=new_rtmsg.route();
    XLOG_ASSERT(existing_route->net() == new_route->net());
    
    typename RefTrie<A, MemorySubnetRoute<A> >::iterator iter = _route_table->lookup_node(existing_route->net());
    if (iter != _route_table->end()) 
    {
    
	MemorySubnetRoute<A> *trie_route = (MemorySubnetRoute<A> *) &(iter.payload());

    	// Create the concise format PA list.
    	PAListRef<A> pa_list = new PathAttributeList<A>(new_rtmsg.attributes());
    	pa_list.register_with_attmgr();

    	AttributeMemory *m= new AttributeMemory();
    	TimerList::system_gettimeofday(&m->when); 
    	m->_attributes = existing_route->attributes(); 
    	trie_route->history.push_front(m);
    	
	if((int)trie_route->history.size() > MAX_HISTORY_SIZE)
        	trie_route->history.pop_back();
    }     
    
    return this->_next_table->replace_route(old_rtmsg, new_rtmsg, (BGPRouteTable<A>*)this);    
}

template<class A>
int
MemoryTable<A>::delete_route(InternalMessage<A> &rtmsg, 
			     BGPRouteTable<A> *caller)
{
    debug_msg("\n         %s\n caller: %s\n rtmsg: %p route: %p\n%s\n",
	      this->tablename().c_str(),
	      caller->tablename().c_str(),
	      &rtmsg,
	      rtmsg.route(),
	      rtmsg.str().c_str());

    XLOG_ASSERT(caller == this->_parent);
    XLOG_ASSERT(this->_next_table != NULL);

    typedef ::AttributeMemory<A> AttributeMemory;
    const SubnetRoute<A> *existing_route=rtmsg.route();
    //log("delete route: " + existing_route->net().str());


    typename RefTrie<A, MemorySubnetRoute<A> >::iterator iter = _route_table->lookup_node(existing_route->net());
    if (iter != _route_table->end()) {
	MemorySubnetRoute<A> *trie_route = (MemorySubnetRoute<A> *) &(iter.payload());
	
	AttributeMemory *m= new AttributeMemory();
    	TimerList::system_gettimeofday(&m->when); 
    	m->_attributes = NULL; // means that the route was deleted at that time.
    	trie_route->history.push_front(m);
	
	if((int)trie_route->history.size() > MAX_HISTORY_SIZE)
		trie_route->history.pop_back();

         this->_next_table->delete_route(rtmsg, (BGPRouteTable<A>*)this);
    } else {
	// we received a delete, but didn't have anything to delete.
	// It's debatable whether we should silently ignore this, or
	// drop the peering.  If we don't hold input-filtered routes in
	// the RIB-In, then this would be commonplace, so we'd have to
	// silently ignore it.  Currently (Sept 2002) we do still hold
	// filtered routes in the RIB-In, so this should be an error.
	// But we'll just ignore this error, and log a warning.
	string s = "Attempt to delete route for net " + existing_route->net().str()
	    + " that wasn't in Memory-Table\n";
	XLOG_WARNING("%s", s.c_str());
	return -1;
    }
    return 0;
}

// Those are not doing anything in particular put propagating
// C++ calls downstream or upstream.

template<class A>
int
MemoryTable<A>::push(BGPRouteTable<A> *caller)
{
    debug_msg("MemoryTable<A>::push\n");
    XLOG_ASSERT(caller == this->_parent);
    XLOG_ASSERT(this->_next_table != NULL);

    return this->_next_table->push((BGPRouteTable<A>*)this);
}

template<class A>
const SubnetRoute<A>*
MemoryTable<A>::lookup_route(const IPNet<A> &net,
			     uint32_t& genid,
			     FPAListRef& pa_list) const
{
    const SubnetRoute<A> *found_route;
    uint32_t found_genid;
    found_route = this->_parent->lookup_route(net, found_genid, pa_list);

    if (found_route == NULL)
	return NULL;
    
    genid = found_genid;
    return found_route;
}

template<class A>
void
MemoryTable<A>::route_used(const SubnetRoute<A>* rt, bool in_use)
{
    this->_parent->route_used(rt, in_use);
}

template<class A>
bool 
MemoryTable<A>::get_next_message(BGPRouteTable<A> *next_table)
{
    BGPRouteTable<A>* parent = this->_parent;

    XLOG_ASSERT(parent);
    XLOG_ASSERT(this->_next_table == next_table);

    return parent->get_next_message(this);
}

template<class A>
string
MemoryTable<A>::dump_state() const {
    string s;
    s  = "=================================================================\n";
    s += "MemoryTable\n";
    s += str() + "\n";
    s += "=================================================================\n";
    s += _route_table->str();
    return s;
} 

template<class A>
string
MemoryTable<A>::str() const
{
    string s = "MemoryTable<A>" + this->tablename();
    return s;
}

template class MemoryTable<IPv4>;
template class MemoryTable<IPv6>;

