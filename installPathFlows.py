# Installs end-to-end bi-directional flows in all switches
def installPathFlows(macHostA, macHostB, pathA2B):
    ##### YOUR CODE HERE #####
    for switch in pathA2B:
        
        #insert forward flow at this switch
        flow1 = ryu_ofctl.FlowEntry()	
        act1 = ryu_ofctl.OutputAction(switch['out_port'])
        flow1.in_port = switch['in_port']	
        flow1.dl_dst = macHostB
        flow1.addAction(act1)
        ryu_ofctl.insertFlow(switch['dpid'], flow1)
        
        #insert r flow at this switch
        flow2 = ryu_ofctl.FlowEntry()	
        act2 = ryu_ofctl.OutputAction(switch['in_port'])
        flow2.in_port = switch['out_port']		
        flow2.dl_dst = macHostA
        flow2.addAction(act2)
        ryu_ofctl.insertFlow(switch['dpid'], flow2)

    return
