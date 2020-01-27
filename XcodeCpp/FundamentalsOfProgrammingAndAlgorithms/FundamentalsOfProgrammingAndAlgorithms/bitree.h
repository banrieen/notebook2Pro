//
//  bitree.h
//  FundamentalsOfProgrammingAndAlgorithms
//
//  Created by lizhen on 2019/10/13.
//  Copyright © 2019 lizhen. All rights reserved.
//

#ifndef bitree_h
#define bitree_h

#include <stdio.h>




// Define a struct for binary tree nodes.
typedef struct BiTreeNode_
{
    void *data;
    struct BiTreeNode_ *left;
    struct BiTreeNode_ *right;
}BiTreenode;

// Define a struct for binary trees.
typedef struct BiTree_{
    int size;
    int (*compare)(const void *key1, const void *key2);
    void (*destory)(void *data);
    BiTreenode *root;
}BiTree;

// Public interface
void bitree_init(BiTree *tree, void (*destory)(void *data));
void bitree_destory(BiTree *tree);
int bitree_ins_left(BiTree *tree, BiTreenode *node, const void *data);
int bitree_ins_right(BiTree *tree, BiTreenode *node, const void *data);
void bitree_rem_left(BiTree *tree, BiTreenode *node);
void bitree_rem_right(BiTree *tree, BiTreenode *node);
int bitree_merge(BiTree *merge, BiTree *left, BiTree *right, const void *data);


#define bitree_size(tree) ((tree)->size)

#define bitree_root(tree) ((tree)->root)

#define bitree_is_eob(node) ((node) == NULL)

#define bitree_is_leaf(node) ((node)->left == NULL && (node)->right == NULL)

#define bitree_data(node) ((node)->data)

#define bitree_left(node) ((node)->left)

#define bitree_right(node) ((node)->right)

#endif // bitree_h
