'''
Created on Feb 19, 2013

@author: Umank
'''
"""
The number of groups are limited (hard-coded) to 8 right now.
"""
import sys
import random
from random import choice
import math
import datetime

class SalsaSim(object):
    """

    """
    def __init__(self, redundancy_factor = None, bad_nodes = None, max_id = (2**63)-1, total_groups = 8, total_nodes = None, target_id = None):
            if(redundancy_factor is None):
                self.redundancy_factor = 3
            else:
                self.redundancy_factor = redundancy_factor
            
            if(bad_nodes is None):
                self.bad_nodes = 200
            else:
                self.bad_nodes = bad_nodes
            
            if(total_nodes is None):
                self.total_nodes = 500
            else:
                self.total_nodes = total_nodes

            self.max_id = max_id
            self.total_groups = total_groups
            
            if (total_groups is not 0) and (not (total_groups & (total_groups - 1))):
                self.total_levels = math.log(total_groups, 2)
                self.total_groups = total_groups
                self.nodes_per_group = self.total_nodes/self.total_groups
            else:
                print ('The number of groups need to be a power of 2..')
                sys.exit()                                   
            
            self.id_per_group = self.max_id/self.total_groups;
            
            if target_id is None:
                self.target_id = random.randrange(max_id)
            else:
                self.target_id = target_id
            if self.bad_nodes >= self.total_nodes:
                print ('Number of Bad nodes equal to or more than Total number of Nodes..')
                sys.exit()
            if self.redundancy_factor < 1:
                print ('Select to run at least one lookup to see results..')
                sys.exit()
            if self.target_id>self.max_id:
                print ('Target ID out of range.')
                sys.exit()
    
    def generate_groups(self):
        groups = []
        for x in range(self.total_groups):
            groups.append('group'+str(x))
        return groups
            
    def assign_idspace(self, groups):
        #id_space = self.generate_id_space()
        #len_idspace = len(id_space)
        #print len_idspace
        #groups = self.generate_groups()
        count_groups = len(groups)
        #print len_groups
        #print id_per_group
        group_dict = {}
        next_stop = self.id_per_group
        next_start = 0
        for group_index in range (count_groups):
            #print str(group_index) + '\n' + str(groups[group_index]) + '\n' + str(id_space[next_start:next_stop])
            #for id_index in range (next_start,id_per_group):
            group_dict[str(groups[group_index])] = {'start':next_start,'stop':next_stop}
            #print group_dict
            next_start = next_start + self.id_per_group
            next_stop = next_stop + self.id_per_group
        return group_dict

    def gen_tree(self, groups):
        pass    
        
    def add_nodes(self, groups, group_dict):
        #groups = self.generate_groups()
        #group_dict = self.assign_idspace()
        node_dict={}
        temp_list=[]
        minint = 0
        maxint = self.id_per_group
        for group_index in range(self.total_groups):
            for nodes_index in range(int(self.nodes_per_group)):            
                node_self_dict={}
                #node_number = str(nodes_group_index)+str(node_index)
                #print node_id
                #print nodes_group_index/10
                node_group = str(groups[group_index])
                node_self_dict['node_group'] = node_group
                #node_self_dict['node_number'] = 'node_'+node_number
                #choose_lcontact_list = group_dict[node_group]
                while True:
                    assigned_id = random.randint(minint,maxint)
                    if assigned_id not in temp_list:
                        break
                #node_self_dict['node_id'] = str(assigned_id)
                temp_list.append(str(assigned_id))
                node_dict[assigned_id] = node_self_dict
            minint = minint + self.id_per_group
            maxint = maxint + self.id_per_group
         
        #print node_dict    
        #print temp_list
        #for ids in temp_list:
        #id_list = node_dict.keys()
        for ids in node_dict.keys():
            #for node_index in range(10):
            #print node_dict
            #local_contact_list = []
            global_contact_list=[]
            chosen_ids = []
            #node_number = str(nodes_group_index)+str(node_index)
            
            home_group = node_dict[ids]['node_group']
            #print home_group
            #print type(home_group)

            
            if home_group == 'group0':
                chosen_ids.append(random.randint(group_dict['group1']['start'],group_dict['group1']['stop']))
                chosen_ids.append(random.randint(group_dict['group2']['start'],group_dict['group3']['stop']))
                chosen_ids.append(random.randint(group_dict['group4']['start'],group_dict['group7']['stop']))
                
            elif home_group == 'group1':                                 
                chosen_ids.append(random.randint(group_dict['group0']['start'],group_dict['group0']['stop']))
                chosen_ids.append(random.randint(group_dict['group2']['start'],group_dict['group3']['stop']))
                chosen_ids.append(random.randint(group_dict['group4']['start'],group_dict['group7']['stop']))
            
            elif home_group == 'group2':
                chosen_ids.append(random.randint(group_dict['group3']['start'],group_dict['group3']['stop']))
                chosen_ids.append(random.randint(group_dict['group0']['start'],group_dict['group1']['stop']))
                chosen_ids.append(random.randint(group_dict['group4']['start'],group_dict['group7']['stop']))

            elif home_group == 'group3':
                chosen_ids.append(random.randint(group_dict['group2']['start'],group_dict['group2']['stop']))
                chosen_ids.append(random.randint(group_dict['group0']['start'],group_dict['group1']['stop']))
                chosen_ids.append(random.randint(group_dict['group4']['start'],group_dict['group7']['stop']))
            
            elif home_group == 'group4':
                chosen_ids.append(random.randint(group_dict['group5']['start'],group_dict['group5']['stop']))
                chosen_ids.append(random.randint(group_dict['group6']['start'],group_dict['group7']['stop']))
                chosen_ids.append(random.randint(group_dict['group0']['start'],group_dict['group3']['stop']))
            
            elif home_group == 'group5':                                 
                chosen_ids.append(random.randint(group_dict['group4']['start'],group_dict['group4']['stop']))
                chosen_ids.append(random.randint(group_dict['group6']['start'],group_dict['group7']['stop']))
                chosen_ids.append(random.randint(group_dict['group0']['start'],group_dict['group3']['stop']))            
            
            elif home_group == 'group6':
                chosen_ids.append(random.randint(group_dict['group7']['start'],group_dict['group7']['stop']))
                chosen_ids.append(random.randint(group_dict['group4']['start'],group_dict['group5']['stop']))
                chosen_ids.append(random.randint(group_dict['group0']['start'],group_dict['group3']['stop']))            

            elif home_group == 'group7':
                chosen_ids.append(random.randint(group_dict['group6']['start'],group_dict['group6']['stop']))
                chosen_ids.append(random.randint(group_dict['group4']['start'],group_dict['group5']['stop']))
                chosen_ids.append(random.randint(group_dict['group0']['start'],group_dict['group3']['stop']))
            
            else:
                pass
            #print chosen_ids
            for x in chosen_ids:
                dist = self.max_id
                last_element = True
                for key in group_dict.keys():
                    #print x
                    #print key
                    if x >= group_dict[key]['start'] and x <= group_dict[key]['stop']:
                        target_group = key
                        #print target_group
                        break
                for con_ids in node_dict.keys():
                    
                    if target_group is node_dict[con_ids]['node_group']:
                        #print x
                        #print ids
                        if con_ids < x:
                            last_element = False
                            temp_dist = x - con_ids
                            if temp_dist < dist:
                                    dist = temp_dist
                                    owner = con_ids
                                    #print 'YESSSSSSSSSSS'
                if last_element is True:
                    temp_list = []
                    for con_ids in node_dict.keys():      
                        if target_group is node_dict[con_ids]['node_group']:
                            temp_list.append(con_ids)
                    temp_list.sort(key=None, reverse=True)    
                    owner = temp_list[0]
                    #print 'WHATTTTTTTTTTTTTTTT'
                #print owner
                global_contact_list.append(owner)
                #print global_contact_list   
                
            #print global_contact_list 
            #print node_dict[ids]     
            node_dict[ids]['global_contacts'] = global_contact_list
        #print node_dict            
        return node_dict    
    
    def lookup(self, node_dict, group_dict):
        #start = str(initiator)
        #print 'Initiator : ' + str(start)
        end = self.target_id
        #print 'Target : ' + str(end)
        
        dist = self.max_id
        greater_check = 0
        for key in group_dict.keys():
            #print x
            #print key
            if end >= group_dict[key]['start'] and end <= group_dict[key]['stop']:
                target_group = key
                #print target_group
                break
        for ids in node_dict.keys():      
            if target_group is node_dict[ids]['node_group']:
                if ids < end:
                    greater_check = greater_check + 1
                    temp_dist = end - ids
                    if temp_dist < dist:
                            dist = temp_dist
                            owner = ids

        if greater_check == 0:
            temp_list = []
            for ids in node_dict.keys():      
                if target_group is node_dict[ids]['node_group']:
                    temp_list.append(ids)
            temp_list.sort(key=None, reverse=True)    
            owner = temp_list[0]

        while True:
            start = choice(list(node_dict.keys()))
            if node_dict[start]['node_group'] != node_dict[owner]['node_group']:
                break
        
        starting_node = start
        
        #new_dict = node_dict
        bad_nodes = []
        for x in range(self.bad_nodes):
            while True:
                bad_node = choice(list(node_dict.keys()))
                if bad_node not in bad_nodes and bad_node != starting_node:
                    #new_dict.pop(bad_node)
                    bad_nodes.append(bad_node)
                    break
        #print '\nList of attacker nodes that drop look-up query: '
        #print bad_nodes
        
        failure = 0
        success = 0
        #print '\nTotal number of lookups: '
        #print self.redundancy_factor
        start_time = datetime.datetime.now()
        started_at = []
        total_hops = 0
        lookup_success = False
        for x in range(self.redundancy_factor):
            nodes_taken=[]
            #print '\nLookup Number #: ' + str(x+1)
            
            if x == 0:
                next_hop = start
                
            else:
                while True:
                    red_start = choice(list(node_dict.keys()))
                    if (node_dict[red_start]['node_group'] == node_dict[start]['node_group']) and (red_start not in started_at):
                        next_hop = red_start
                        break    
                    
            started_at.append(next_hop)
            #print 'Starting at ' + str(next_hop)
            
            not_found = True
            while not_found:

                if next_hop in bad_nodes:
                    #print 'Failed'
                    failure = failure + 1
                    #print 'Total Execution Time : ' + str(total_time.microseconds)
                    break
                else:
                    if node_dict[next_hop]['node_group'] is not node_dict[owner]['node_group']:
                        temp_node_dist = self.max_id
                        for temp_node in node_dict[next_hop]['global_contacts']:
                            node_dist = abs(temp_node - owner)
                            if node_dist < temp_node_dist:
                                temp_node_dist = node_dist
                                next_node = temp_node
                        #next_node = choice(node_dict[next_hop]['global_contacts'])
                        next_hop = next_node
                        nodes_taken.append(next_hop)
                        #print 'Next Hop : ' + str(next_hop)
                    elif node_dict[next_hop]['node_group'] is node_dict[owner]['node_group']:
                        not_found = False
                        lookup_success = True
                        success = success + 1
                        #print node_dict[end]
                        #print 'Success'
                        #end_time = datetime.datetime.now()
                        #time = end_time - start_time
                        #print 'Total Execution Time : ' + str(total_time.microseconds)
                    else:
                        print ('Unexpected Error.. Node not found.. Please try again.')
            total_hops = total_hops + len(nodes_taken)
            #print 'Number of Hops this lookup : ' + str(total_hops)
        
        hops_per_lookup = float(total_hops/self.redundancy_factor)                
        end_time = datetime.datetime.now()
        total_time = end_time - start_time
        lookup_status = {'Attacker Nodes':bad_nodes,'Number_of_lookups':self.redundancy_factor,'Target':self.target_id,'Initiator':starting_node,'Success':success,'Failure':failure,'Average_Hops':hops_per_lookup,'X_Time_in_microseconds':total_time.microseconds,'Found':lookup_success}
        return lookup_status
    
    def get_rate(self, lookup_status):
        bad_nodes = (float(self.bad_nodes)/self.total_nodes)*100
        success_rate = (float(lookup_status['Success'])/self.redundancy_factor)*100
        failure_rate = (float(lookup_status['Failure'])/self.redundancy_factor)*100
        rate = {'Success':success_rate,'Failure':str(failure_rate)+'%','Attackers':str(bad_nodes)+'%'}
        return rate

if __name__ == '__main__':
    #print 'This is MAIN..!!'
    count = 20
    fin_num = 0
    fin_hops = 0
    found = 0
    for x in range(count):
        sys.stdout.flush()
        #print '\nRunning Loop ' + str(x+1)
        obj1 = SalsaSim()
        #print obj1.generate_id_space()
        #print obj1.generate_groups()
        sys.stdout.write('Running Loop #{0}.. {1} loops remaining..\r'.format(x+1, count-x-1))
        groups = obj1.generate_groups()
        group_dict = obj1.assign_idspace(groups)
        node_dict = obj1.add_nodes(groups, group_dict)
        #print 'This is the Network Map..'
        #print node_dict
        #print '\nPerforming Lookup Now..'
        lookup_status = obj1.lookup(node_dict, group_dict)
        #print '\nTotal Lookup Stats: ' + str(lookup_status)
        #print '\nSuccess Rate in Percentage: '
        rate = obj1.get_rate(lookup_status)
        #print rate
        fin_num = fin_num + rate['Success']
        fin_hops = fin_hops + lookup_status['Average_Hops']
        if lookup_status['Found']:    
            found = found + 1
            #print found
        #print '\nEnd of Loop ' + str(x+1)
    res = fin_num/count
    hops = fin_hops/count
    total_found = float((found*100)/count)
    print ('\n\nCompletion Statistics:\n\tRedundancy = ' + str(obj1.redundancy_factor) + ', Total Nodes = ' + str(obj1.total_nodes) + ', Fraction of Attackers = ' + str(rate['Attackers']) + ', Successful Lookups = '+ str(res) + '%.')
    print ('\nInitiator = ' + str(lookup_status['Initiator']) + '\nTarget = ' + str(lookup_status['Target']))
    #print '\nAverage Hop Count = ' + str(hops)
    print ('\nAverage Successful Route Completion Rate = ' + str(total_found) +'%')
    print ('\nEnd of Execution..!!')