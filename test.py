import requests

def get_request(id):
	r = requests.get("https://nodes-on-nodes-challenge.herokuapp.com/nodes/"+id).json()
	return(r)


src=get_request("089ef556-dfff-4ff2-9733-654645be56fe")[0]

#stack for DFS
st=[]
st.append(src['id'])

#This dictionary ensures we don't visit the same node twice and also keeps track of number of incoming edges. 
visited={}

while(st):
	top=st.pop()
	if(top not in visited):
		
		if(top!=src):
			visited[top]=1

		else:
			#source node does not have an incoming edge
			visited[top]=0
		current=get_request(top)[0]
		children=current['child_node_ids']
		for child in children:
			st.append(child)

	else:
		visited[top]+=1
		
print("Total number of unique node ids- ",len(visited))
print("Most common node id- ",max(visited,key=visited.get))


