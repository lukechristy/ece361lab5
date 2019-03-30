import ryu_ofctl

dpid = '1'	#identifies the controller

# Flow for packets h1->h3 (sends copy to h2)
flow1 = ryu_ofctl.FlowEntry()	
act1 = ryu_ofctl.OutputAction(3)	#output to port 3
act2 = ryu_ofctl.OutputAction(2)	#forward copy to port 2
flow1.in_port = 1					#packets coming from port 1
flow1.dl_dst = "00:00:00:00:00:03"	#that are destined for port 3
flow1.addAction(act1)
flow1.addAction(act2)
ryu_ofctl.insertFlow(dpid, flow1)	#insert flow1

# Flow for packets h3->h1 (sends copy to h2)
flow2 = ryu_ofctl.FlowEntry()
act3 = ryu_ofctl.OutputAction(1)	#output to port 1
act4 = ryu_ofctl.OutputAction(2)	#forward copy to port 2
flow2.in_port = 3					#packets coming from port 3
flow2.dl_dst = "00:00:00:00:00:01"	#that are destined for port 1
flow2.addAction(act3)
flow2.addAction(act4)
ryu_ofctl.insertFlow(dpid, flow2)	#insert flow2
