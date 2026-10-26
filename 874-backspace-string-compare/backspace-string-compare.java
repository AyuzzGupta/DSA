class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1;
        int j = t.length() - 1;

        int skipS = 0;
        int skipT = 0;

        while (i >= 0 || j >= 0) {  // Outer loop

        while (i >= 0) {        // Inner loop: s
            if (s.charAt(i) == '#') {
                skipS++;
                i--;
            }
            else if (skipS > 0) {
                skipS--;
                i--;
            }
            else {
                break;
            }
        }

        while (j >= 0) {        // Inner loop: t
            if (t.charAt(j) == '#') {
                skipT++;
                j--;
            }
            else if (skipT > 0) {
                skipT--;
                j--;
            }
            else {
                break;
            }
        }

        // Yahan comparison hoga
        if (i >= 0 && j >= 0 && s.charAt(i) != t.charAt(j)) {
            return false;
        }

        // Ek string khatam, doosri nahi
        if ((i >= 0) != (j >= 0)) {
            return false;
        }

        // Dono valid characters compare ho gaye
        i--;
        j--;
    } // Outer loop dobara chalega

    return true;
    }
}