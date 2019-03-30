import ryu_ofctl

dpid = '1'	#identifies the controller

# Flow for packets h1->h3 (blocks traffic)
flow1 = ryu_ofctl.FlowEntry()	
flow1.in_port = 1					#packets coming from port 1
flow1.dl_dst = "00:00:00:00:00:03"	#that are destined for port 3
ryu_ofctl.insertFlow(dpid, flow1)	#insert flow1

# Flow for packets h3->h1 (blocks traffic)
flow2 = ryu_ofctl.FlowEntry()
flow2.in_port = 3					#packets coming from port 3
flow2.dl_dst = "00:00:00:00:00:01"	#that are destined for port 1
ryu_ofctl.insertFlow(dpid, flow2)	#insert flow2
