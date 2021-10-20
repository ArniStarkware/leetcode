#include <tuple>
#include<algorithm>
#include <iostream>
/*
Note: I do not understand how some of the solutions pass the testing.
*/


// Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
    struct TreeNode_details{int depth; int diameter;};
    
    TreeNode_details get_TreeNode_details(TreeNode *node) {
        int depth{0};
        int diameter{0};
        int left_depth{0};
        int left_diameter{0};

        if (node->left != nullptr){
            TreeNode_details left_details{get_TreeNode_details(node->left)};
            left_depth = left_details.depth;
            left_diameter = left_details.diameter;
        }
        else
        {
            left_depth = -1;
            left_diameter = -1;
        }
        int right_depth{0};
        int right_diameter{0};

        if (node->right != nullptr){
            TreeNode_details right_details{get_TreeNode_details(node->right)};
            right_depth = right_details.depth;
            right_diameter = right_details.diameter;
        }
        else
        {
            right_depth = -1;
            right_diameter = -1;
        }
        depth = std::max({0,right_depth+1,left_depth+1});
        diameter = std::max({0,right_diameter,left_diameter,right_depth+left_depth+2});

        return TreeNode_details{depth,diameter};
    }

    
    int diameterOfBinaryTree(TreeNode* root) {
        TreeNode_details rootDetails{get_TreeNode_details(root)};
        return rootDetails.diameter;
    }
    
};