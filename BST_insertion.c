

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

*/
struct node *newNode(int item) 
{ 
    struct node *temp =  (struct node *)malloc(sizeof(struct node)); 
    temp->data = item; 
    temp->left = temp->right = NULL; 
    return temp; 
} 

struct node* insert( struct node* root, int data ) { 
    /* If the tree is empty, return a new node */
    if (root == NULL) return newNode(data); 
  
    /* Otherwise, recur down the tree */
    if (data < root->data) 
        root->left  = insert(root->left, data); 
    else if (data > root->data) 
        root->right = insert(root->right, data);    
  
    /* return the (unchanged) node pointer */
    return root; 
} 

