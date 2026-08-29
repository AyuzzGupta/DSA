bool isPalindrome(struct ListNode* head) {
    
    int arr[100000];
    int i = 0;

    // Linked list ke values array mein store karo
    while (head != NULL) {
        arr[i] = head->val;
        i++;
        head = head->next;
    }

    // Dono ends se compare karo
    int left = 0;
    int right = i - 1;

    while (left < right) {
        if (arr[left] != arr[right]) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}