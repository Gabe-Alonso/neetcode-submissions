

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int max_len = 0;
        Hashtable<String, Integer> used = new Hashtable<String, Integer>();
        for (int i = 0; i < s.length(); i++) {
            String cur_char = s.substring(i, i+1);
            System.out.println("Looking at: " + cur_char);
            if (used.containsKey(cur_char)){
                for (int j = start; start < used.get(cur_char) + 1; start++){
                    if (!cur_char.equals(s.substring(start, start+1))){
                        used.remove(s.substring(start, start+1));
                    }
                }
                used.replace(cur_char, i);
            } else {
                used.put(cur_char, i);
            }
            max_len = Math.max(max_len, i - start + 1);
            System.out.println(s.substring(start, i + 1));
            System.out.println(used);
        }


        return max_len;
    }
}
