import java.util.HashMap;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split("\\s+");
        
        // अगर अक्षर और शब्दों की गिनती बराबर नहीं है, तो पैटर्न नहीं बन सकता
        if (pattern.length() != words.length) {
            return false;
        }

        // आपके तरीके को चलाने के लिए दो पॉकेट्स (Maps) की जरूरत है
        HashMap<Character, String> charToWord = new HashMap<>();
        HashMap<String, Character> wordToChar = new HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            char ch = pattern.charAt(i); // charAt(i) को एक वेरिएबल में रख लिया
            String word = words[i];

            // 1. अगर यह अक्षर पहले आ चुका है, तो चेक करो कि क्या इसके साथ वही शब्द है या नहीं
            if (charToWord.containsKey(ch)) {
                if (!charToWord.get(ch).equals(word)) { // यहाँ .equals() सही है क्योंकि शब्द (String) ऑब्जेक्ट है
                    return false; // अगर पुराना शब्द मैच नहीं हुआ तो गलत पैटर्न है
                }
            } 
            // 2. अगर यह अक्षर पहली बार आया है, लेकिन शब्द किसी और अक्षर के साथ पहले ही बुक हो चुका है
            else if (wordToChar.containsKey(word)) {
                return false; 
            } 
            // 3. अगर दोनों नए हैं, तो दोनों को अपनी पॉकेट में याद रख लो (जैसा आपका 'else' पार्ट था)
            else {
                charToWord.put(ch, word);
                wordToChar.put(word, ch);
            }
        }

        return true; // अगर पूरा लूप बिना किसी गड़बड़ के खत्म हो गया
    }
}
