// -*- c-basic-offset: 4; tab-width: 8; indent-tabs-mode: t -*-

// Copyright (c) 2001-2009 XORP, Inc.
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License, Version 2, June
// 1991 as published by the Free Software Foundation. Redistribution
// and/or modification of this program under the terms of any other
// version of the GNU General Public License is not permitted.
// 
// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. For more details,
// see the GNU General Public License, Version 2, a copy of which can be
// found in the XORP LICENSE.gpl file.
// 
// XORP Inc, 2953 Bunker Hill Lane, Suite 204, Santa Clara, CA 95054, USA;
// http://xorp.net

// $XORP: xorp/bgp/route_table_ribin.hh,v 1.32 2009/01/05 18:30:43 jtc Exp $

#ifndef __BGP_ROUTE_TABLE_MEMORY_HH__
#define __BGP_ROUTE_TABLE_MEMORY_HH__


#include <map>
#include "libxorp/eventloop.hh"
#include "route_table_base.hh"
#include "crash_dump.hh"
#include "bgp_trie.hh"
#include "subnet_route.hh"
#include "libxorp/timeval.hh"

#define MAX_HISTORY_SIZE 10
template <class A>
class AttributeMemory {
public:
	TimeVal when;
	
	/**
	* _attributes is a pointer to the path attribute list for this
	* route.  The actual data storage for the path attribute list is
	* handled inside the attribute manager
	*/
	
	PAListRef<A> _attributes;
};

template<class A>
class MemorySubnetRoute : public SubnetRoute<A> {
public:
    	MemorySubnetRoute(const IPNet<A> &net,
		       const PAListRef<A> attributes) :
	SubnetRoute<A>(net, attributes,NULL) {}
	
	list< AttributeMemory<A> > history;
};

/**
 * @short Specialized BGPRouteTable that stores the memory of 
 $ routes announced/withdrawn from a BGP peer.
 *
 * The XORP BGP is internally implemented as a set of pipelines
 * consisting of a series of BGPRouteTables.  Each pipeline receives
 * routes from a BGP peer, stores them, and applies filters to them to
 * modify the routes.  Then the pipelines converge on a single
 * decision process, which decides which route wins amongst possible
 * alternative routes.  After decision, the winning routes fanout
 * again along a set of pipelines, again being filtered, before being
 * transmitted to peers.
 *
 */ 

template<class A>
class MemoryTable : public BGPRouteTable<A> {
public:
    MemoryTable(string tablename, Safi safi);
    ~MemoryTable();
    /**
     * Remove all the stored routes. Used to flush static routes only.
     */
    void flush();

    /* this version is deprecated  - we only use messages between stages */
    int add_route(InternalMessage<A>& /*rtmsg*/,
		  BGPRouteTable<A>* /*caller*/);

    int replace_route(InternalMessage<A> & /*old_rtmsg*/,
		      InternalMessage<A> & /*new_rtmsg*/,
		      BGPRouteTable<A> * /*caller*/ );

    /* this version is deprecated  - we only use messages between stages */
    int delete_route(InternalMessage<A>& /*rtmsg*/,
		     BGPRouteTable<A>* /*caller*/);

    int push(BGPRouteTable<A> *caller);
    int delete_add_routes();
    const SubnetRoute<A> *lookup_route(const IPNet<A> &net, 
				       uint32_t& genid,
				       FPAListRef& pa_list) const;
    void route_used(const SubnetRoute<A>* route, bool in_use);

    BGPRouteTable<A> *parent() { return NULL; }

    RouteTableType type() const { return RIB_IN_TABLE; }

    string str() const;

    bool get_next_message(BGPRouteTable<A> */*next_table*/);
    
    bool dump_next_route(DumpIterator<A>& dump_iter);

    int route_count() const {
	return _route_table->route_count();
    }

    BgpTrie<A>& trie() const {
	return *_route_table;
    }

    uint32_t genid() const {
	return _genid;
    }

    string dump_state() const;

private:

    BgpTrie<A>* _route_table;
    uint32_t _genid;
    uint32_t _table_version;

};

#endif // __BGP_ROUTE_TABLE_MEMORY_HH__
