/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* mid=head;
        int count=1;
        while(head!=NULL)
        {
            head=head->next;
            if (!(count++&1))
                mid=mid->next;
        }
        return mid;
    }
};
