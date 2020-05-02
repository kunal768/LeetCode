class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groupAnagrams = new ArrayList<>();
        HashMap<String,List<String>> map = new HashMap<>();
        
        // sort each string
        for(String curr : strs){
        	char[] characters = curr.toCharArray();
        	Arrays.sort(characters);
        	String sorted = new String(characters);
        	if(!map.contains(sorted)){
        		map.put(sorted,new ArrayList<>());
        	}
        	map.get(sorted).add(curr);
        }
        groupAnagrams.add(map.values());
        return groupAnagrams;
    }
}

// Understood Senpai :') 
// You are <3  @KevinNaughtonJr.
// and i just subscribed you on YT
