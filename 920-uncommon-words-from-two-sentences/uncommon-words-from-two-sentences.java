import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        String[] s11 = s1.split(" ");
        String[] s12 = s2.split(" ");
        
        // दोनों एरे के शब्दों को एक साथ मिलाने के लिए
        int totalLength = s11.length + s12.length;
        String[] allWords = new String[totalLength];
        
        System.arraycopy(s11, 0, allWords, 0, s11.length);
        System.arraycopy(s12, 0, allWords, s11.length, s12.length);
        
        List<String> result = new ArrayList<>();
        
        // हर शब्द को उठाकर बाकी सब से तुलना करेंगे (Nested Loop)
        for (int i = 0; i < allWords.length; i++) {
            int count = 0;
            for (int j = 0; j < allWords.length; j++) {
                if (allWords[i].equals(allWords[j])) {
                    count++;
                }
            }
            // अगर शब्द पूरी दोनों लाइनों में सिर्फ 1 ही बार आया है
            if (count == 1) {
                result.add(allWords[i]);
            }
        }
        
        // लिस्ट को वापस स्ट्रिंग एरे में बदलें
        return result.toArray(new String[0]);
    }
}
