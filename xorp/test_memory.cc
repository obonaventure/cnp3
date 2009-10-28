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

#ident "$XORP: xorp/bgp/test_ribin.cc,v 1.44 2009/01/05 18:30:43 jtc Exp $"

#include "bgp_module.h"

#include "libxorp/xorp.h"
#include "libxorp/xorpfd.hh"
#include "libxorp/eventloop.hh"
#include "libxorp/xlog.h"
#include "libxorp/test_main.hh"

#ifdef HAVE_PWD_H
#include <pwd.h>
#endif

#include "bgp.hh"
#include "route_table_base.hh"
#include "route_table_ribin.hh"
#include "route_table_memory.hh"
#include "route_table_debug.hh"
#include "path_attribute.hh"
#include "local_data.hh"
#include "dump_iterators.hh"


bool
validate_reference_file(string reference_file, string output_file,
			string testname);

bool
test_memory(TestInfo& /*info*/)
{
#ifndef HOST_OS_WINDOWS
    struct passwd *pwd = getpwuid(getuid());
    string filename = "/tmp/test_memory.";
    filename += pwd->pw_name;
#else
    char *tmppath = (char *)malloc(256);
    GetTempPathA(256, tmppath);
    string filename = string(tmppath) + "test_memory";
    free(tmppath);
#endif

    EventLoop eventloop;
    BGPMain bgpmain(eventloop);
    LocalData localdata(bgpmain.eventloop());
    Iptuple iptuple;
    BGPPeerData *pd1 = new BGPPeerData(localdata, iptuple, AsNum(0), IPv4(),0);
    BGPPeer peer1(&localdata, pd1, NULL, &bgpmain);
    PeerHandler handler1("test1", &peer1, NULL, NULL);
    BGPPeerData *pd2 = new BGPPeerData(localdata, iptuple, AsNum(0), IPv4(),0);
    BGPPeer peer2(&localdata, pd2, NULL, &bgpmain);
    PeerHandler handler2("test2", &peer2, NULL, NULL);

    //trivial plumbing
    RibInTable<IPv4> *ribin 
	= new RibInTable<IPv4>("RIB-IN", SAFI_UNICAST, &handler1);
    MemoryTable<IPv4>* memory_table
	 = new MemoryTable<IPv4>("MEMORY", SAFI_UNICAST, (BGPRouteTable<IPv4>*)ribin);
    DebugTable<IPv4>* debug_table
	 = new DebugTable<IPv4>("D1", (BGPRouteTable<IPv4>*)memory_table);
    ribin->set_next_table(memory_table);
    memory_table->set_next_table(debug_table);
    debug_table->set_output_file(filename);
    debug_table->set_canned_response(ADD_USED);
    debug_table->set_is_winner(true);

    //create a load of attributes 
    IPNet<IPv4> net1("1.0.1.0/24");
    IPNet<IPv4> net2("1.0.2.0/24");

    IPv4 nexthop1("2.0.0.1");
    NextHopAttribute<IPv4> nhatt1(nexthop1);

    IPv4 nexthop2("2.0.0.2");
    NextHopAttribute<IPv4> nhatt2(nexthop2);

    OriginAttribute igp_origin_att(IGP);

    ASPath aspath1;
    aspath1.prepend_as(AsNum(1));
    aspath1.prepend_as(AsNum(2));
    aspath1.prepend_as(AsNum(3));
    ASPath foo("3,2,1");
    assert (foo == aspath1);
    ASPathAttribute aspathatt1(aspath1);

    ASPath aspath2;
    aspath2.prepend_as(AsNum(3));
    aspath2.prepend_as(AsNum(4));
    aspath2.prepend_as(AsNum(5));
    ASPathAttribute aspathatt2(aspath2);

    FPAList4Ref palist1 =
	new FastPathAttributeList<IPv4>(nhatt1, aspathatt1, igp_origin_att);

    FPAList4Ref palist2 =
	new FastPathAttributeList<IPv4>(nhatt2, aspathatt1, igp_origin_att);

    FPAList4Ref palist3, palist4;

    PAListRef<IPv4> dummy_palist;
    dummy_palist.create_attribute_manager();

    PolicyTags policytags;


    //================================================================
    //Test1: trivial add and delete
    //================================================================
    //add a route
    debug_table->write_comment("TEST 1");
    ribin->add_route(net1, palist1, policytags);

    //check we only ended up with one copy of the PA list
    assert(dummy_palist.number_of_managed_atts() == 1);

    //check there's one route in the RIB-IN
    assert(ribin->route_count() == 1);

    debug_table->write_separator();

    //delete the route
    ribin->delete_route(net1);

    //check there's still one copy of the PA list
    //the one that's used by the memory trie 
    assert(dummy_palist.number_of_managed_atts() == 1);

    //check there are no routes in the RIB-IN
    assert(ribin->route_count() == 0);
    
    //but that there is still a route in the MEMORY
    assert(memory_table->route_count() == 1);

    debug_table->write_separator();
    //================================================================
    //Test2: trivial add , replace and delete
    //================================================================
    //add a route
    debug_table->write_comment("TEST 2");
    debug_table->write_comment("ADD FIRST ROUTE");
    ribin->add_route(net1, palist1, policytags);
    palist1 = 0;

    //check there's still one route in the RIB-IN
    assert(ribin->route_count() == 1);
    
    //check as well that there's still one route in the MEMORY
    assert(memory_table->route_count() == 1);

    //check we only ended up with two copies of the same PA list
    //One for the RIBIN and one for the MEMORY
    assert(dummy_palist.number_of_managed_atts() == 1);

    debug_table->write_separator();

    //add the same route again - should be treated as an update, and
    //trigger a replace operation
    debug_table->write_comment("ADD MODIFIED FIRST ROUTE");
    ribin->add_route(net1, palist2, policytags);

    //check we only ended up with two pointers of the same PA list 
    //One for the RIBIN and one for the MEMORY
    assert(dummy_palist.number_of_managed_atts() == 2);

    //check there's still one route in the RIB-IN
    //and one route in the MEMORY
    assert(ribin->route_count() == 1);
    assert(memory_table->route_count() == 1);

    debug_table->write_separator();

    //delete the route
    debug_table->write_comment("DELETE ROUTE");
    ribin->delete_route(net1);

    //check there's still two pointers on the two PA list: those from MEMORY
    assert(dummy_palist.number_of_managed_atts() == 2);

    //check there are no routes in the RIB-IN
    //and one route in the MEMORY (with 2 attributes in memory)
    assert(ribin->route_count() == 0);
    assert(memory_table->route_count() == 1);

    debug_table->write_separator();

    palist2 = 0;
    
    //================================================================
    //Test3: trivial add two routes, then drop peering
    //================================================================
    //add a route
    debug_table->write_comment("TEST 3");
    palist1 =
	new FastPathAttributeList<IPv4>(nhatt1, aspathatt1, igp_origin_att);

    palist2 =
	new FastPathAttributeList<IPv4>(nhatt2, aspathatt1, igp_origin_att);

    debug_table->write_comment("ADD FIRST ROUTE");
    ribin->add_route(net1, palist1, policytags);
    palist1 = 0;

    debug_table->write_comment("ADD SECOND ROUTE");
    ribin->add_route(net2, palist2, policytags);
    palist2 = 0;

    //check there are two routes in the RIB-IN
    assert(ribin->route_count() == 2);

    //check we only ended up with two PA lists
    assert(dummy_palist.number_of_managed_atts() == 2);

    debug_table->write_separator();

    debug_table->write_comment("NOW DROP THE PEERING");

    ribin->ribin_peering_went_down();
    while (bgpmain.eventloop().events_pending()) {
	bgpmain.eventloop().run();
    }

    debug_table->write_separator();

    //================================================================
    //Test4: trivial add two routes, then do a route dump
    //================================================================
    ribin->ribin_peering_came_up();
    //add a route
    debug_table->write_comment("TEST 4");
    palist1 =
	new FastPathAttributeList<IPv4>(nhatt1, aspathatt1, igp_origin_att);

    palist2 =
	new FastPathAttributeList<IPv4>(nhatt2, aspathatt1, igp_origin_att);

    //routes will only be dumped if they won at decision
    debug_table->write_comment("ADD FIRST ROUTE");
    ribin->add_route(net1, palist1, policytags);

    debug_table->write_comment("ADD SECOND ROUTE");
    ribin->add_route(net2, palist2, policytags);
    palist1 = 0;

    //check there are two routes in the RIB-IN
    assert(ribin->route_count() == 2);

    //check we only ended up with two PA lists
    assert(dummy_palist.number_of_managed_atts() == 2);
    palist2 = 0;

    debug_table->write_separator();

    debug_table->write_comment("NOW DO THE ROUTE DUMP");

    list <const PeerTableInfo<IPv4>*> peers_to_dump;
    PeerTableInfo<IPv4>* pti = new PeerTableInfo<IPv4>(NULL, &handler1, 
						       ribin->genid());
    peers_to_dump.push_back(pti);
    DumpIterator<IPv4>* dump_iter 
	= new DumpIterator<IPv4>(&handler2, peers_to_dump);
    while (ribin->dump_next_route(*dump_iter)) {
	while (bgpmain.eventloop().events_pending()) {
	    bgpmain.eventloop().run();
	}
    }
    delete dump_iter;
    delete pti;

    debug_table->write_separator();

    debug_table->write_comment("DELETE THE ROUTES AND CLEAN UP");

    ribin->delete_route(net1);
    ribin->delete_route(net2);


    debug_table->write_separator();
    //================================================================
    //Test5: IGP nexthop changes
    //================================================================

    debug_table->write_comment("TEST 5");
    debug_table->write_comment("IGP NEXTHOP CHANGES");
    palist1 =
	new FastPathAttributeList<IPv4>(nhatt1, aspathatt1, igp_origin_att);

    palist2 =
	new FastPathAttributeList<IPv4>(nhatt2, aspathatt1, igp_origin_att);

    debug_table->write_comment("ADD FIRST ROUTE");
    ribin->add_route(net1, palist1, policytags);
    palist1 = 0;

    debug_table->write_comment("ADD SECOND ROUTE");
    ribin->add_route(net2, palist2, policytags);
    palist2 = 0;

    //check there are two routes in the RIB-IN
    assert(ribin->route_count() == 2);

    debug_table->write_separator();
    debug_table->write_comment("NEXTHOP 2.0.0.2 CHANGES");
    //this should trigger a replace
    ribin->igp_nexthop_changed(nexthop2);
    while (bgpmain.eventloop().events_pending()) {
	bgpmain.eventloop().run();
    }
    debug_table->write_separator();
    debug_table->write_comment("NEXTHOP 2.0.0.1 CHANGES");
    //this should trigger a replace
    ribin->igp_nexthop_changed(nexthop1);
    while (bgpmain.eventloop().events_pending()) {
	bgpmain.eventloop().run();
    }

    IPv4 nexthop3("1.0.0.1");
    debug_table->write_separator();
    debug_table->write_comment("NEXTHOP 1.0.0.1 CHANGES");
    //this should have no effect
    ribin->igp_nexthop_changed(nexthop3);
    while (bgpmain.eventloop().events_pending()) {
	bgpmain.eventloop().run();
    }

    IPv4 nexthop4("3.0.0.1");
    debug_table->write_separator();
    //this should have no effect
    debug_table->write_comment("NEXTHOP 3.0.0.1 CHANGES");
    ribin->igp_nexthop_changed(nexthop4);
    while (bgpmain.eventloop().events_pending()) {
	bgpmain.eventloop().run();
    }

    debug_table->write_separator();

    //Add two more routes with same nexthop as net1

    IPNet<IPv4> net3("1.0.3.0/24");
    IPNet<IPv4> net4("1.0.4.0/24");
    //palist1 has the same palist as the route for net1
    palist3 =
	new FastPathAttributeList<IPv4>(nhatt1, aspathatt1, igp_origin_att);

    //palist1 has the same nexthop, but different palist as the route for net1
    palist4 =
	new FastPathAttributeList<IPv4>(nhatt1, aspathatt2, igp_origin_att);

    debug_table->write_comment("ADD THIRD ROUTE");
    ribin->add_route(net3, palist3, policytags);
    palist3 = 0;

    //check there are 3 routes in the RIB-IN
    assert(ribin->route_count() == 3);

    debug_table->write_comment("ADD FOURTH ROUTE");
    ribin->add_route(net4, palist4, policytags);
    palist4 = 0;

    //check there are 4 routes in the RIB-IN
    assert(ribin->route_count() == 4);

    debug_table->write_separator();
    debug_table->write_separator();
    debug_table->write_comment("NEXTHOP 2.0.0.1 CHANGES");
    //this should trigger three a replaces
    ribin->igp_nexthop_changed(nexthop1);
    while (bgpmain.eventloop().events_pending()) {
	bgpmain.eventloop().run();
    }

    debug_table->write_separator();
    debug_table->write_comment("DELETE THE ROUTES AND CLEAN UP");

    ribin->delete_route(net1);
    ribin->delete_route(net2);
    ribin->delete_route(net3);
    ribin->delete_route(net4);

    debug_table->write_separator();

    //================================================================

    debug_table->write_comment("SHUTDOWN AND CLEAN UP");
    delete ribin;
    delete debug_table;

    return true;
    //return validate_reference_file("/test_ribin.reference", filename, "RIBIN");
}
