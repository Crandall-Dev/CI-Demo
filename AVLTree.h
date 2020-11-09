/*
 *  Yet another AVL tree edition
 * 
 *  Contributors:
 *      Aaron S. Crandall <acrandal@wsu.edu> - 2018
 * 
 */

#ifndef __AVLTree_H
#define __AVLTree_H

#include <ostream>
#include <algorithm>     // Includes a max(a,b) function
#include <exception>

#include "AVLNode.h"

// AVLTree class
// ******************PUBLIC OPERATIONS*********************
// bool empty( )          --> Test for empty tree
// int size( )            --> Quantity of elements in tree
// int height( )          --> Height of the tree (nullptr == -1)
// void add( x )          --> Insert new value x
// void remove( x )       --> Remove node with value x
// void clear ( )         --> Removes all elements from tree
// bool contains( x )     --> Return true if x is present
// T findMin( )           --> Return smallest item value
// T findMax( )           --> Return largest item value
// void printPreOrder( )  --> Print tree in pre order to an ostream
// void ~AVLTree( )       --> Big Five Destructor
// AVLTree( )             --> Basic constructor


template <typename T>
class AVLTree
{
private:
    AVLNode<T> * _root;

public:
    AVLTree() : _root(nullptr) {}    // initializes root to nullptr

    ~AVLTree() {
        clear();
    }

    /* Returns true if the tree is empty */
    bool empty() {
        if(this->_root == nullptr)
            return true;
        return false;
    }

    void add(const T & newVal) {
        add(this->_root, newVal);
    }

    void remove(const T & remVal) {
        remove(this->_root, remVal);
    }

    void clear() {
        clear(this->_root);
    }

    bool contains(const T & findVal) {
        return contains(this->_root, findVal);
    }

    int height() {
        return height( this->_root );
    }

    T findMin() {
        return findMin(this->_root);
    }

    T findMax() {
        return findMax(this->_root);
    }

    void printPreOrder(std::ostream& out) {
        printPreOrder(this->_root, out);
    }

    int size() {
        return(size(this->_root));
    }

// *************** Private /internal function implementation ******* //

private:
    void add(AVLNode<T> * & t, const T & newVal) {
        if(t == nullptr)
            t = new AVLNode<T>( newVal );
        else if( newVal < t->val )
            add(t->left, newVal);
        else if( newVal > t->val )
            add(t->right, newVal);

        balance(t);
    }

    void remove(AVLNode<T> * & t, const T & remVal) {
        if( t == nullptr )
            return;

        if( remVal < t->val )
            remove( t->left, remVal );
        else if( t->val < remVal )
            remove( t->right, remVal );
        else if( t->left != nullptr && t->right != nullptr ) // Two children
        {
            t->val = findMin( t->right );
            remove( t->right, t->val );
        }
        else
        {
            AVLNode<T> * oldNode = t;
            t = ( t->left != nullptr ) ? t->left : t->right;
            delete oldNode;
            oldNode = nullptr;
        }

        balance( t );
    }

    void clear(AVLNode<T> * & t) {
        if(t == nullptr)
            return;
        else {
            clear(t->left);
            clear(t->right);
            delete t;
            t = nullptr;
        }
    }

    bool contains(AVLNode<T> * & t, const T & findVal) {
        if( t == nullptr )
            return false;
        else if(t->val == findVal)
            return true;
        else {
            return( contains(t->left, findVal) || contains(t->right, findVal) );
        }
    
    }

    int size(AVLNode<T> * & t) {
        if(t == nullptr)
            return 0;
        else
            return 1 + size(t->left) + size(t->right);
    }

    void printPreOrder(AVLNode<T> * & t, std::ostream& out)
    {
        if( t != nullptr )
        {
            out << t->val << " ";
            printPreOrder(t->left, out);
            printPreOrder(t->right, out);
        }
    }

    // Freebie: neat little function to safely get a node's height
    int height( AVLNode<T> * t ) const
    {
        return t == nullptr ? -1 : t->height;
    }

    T findMin(AVLNode<T> * t) {
        if(t == nullptr)
            throw std::out_of_range("No nodes in tree");
        else if(t->left != nullptr)
            return findMin(t->left);
        else
            return t->val;
    }

    T findMax(AVLNode<T> * t) {
        if(t == nullptr)
            throw std::out_of_range("No nodes in tree");
        else if(t->right != nullptr)
            return findMax(t->right);
        else
            return t->val;
    }

    void balance( AVLNode<T> * & t )
    {   
        if( t == nullptr )
            return;

        if( height( t->left ) - height( t->right ) == 2 )
        {   
            if( height( t->left->left ) >= height( t->left->right ) )
                rotateWithLeftChild( t );
            else
                doubleWithLeftChild( t );
        }
        else
        if( height( t->right ) - height( t->left ) == 2 )
        {   
            if( height(t->right->right) >= height( t->right->left ) )
                rotateWithRightChild( t );
            else
                doubleWithRightChild( t );
        }

        t->height = std::max( height( t->left ), height( t->right ) ) + 1;
    }

    /**
     * Rotate binary tree node with left child.
     * For AVL trees, this is a single rotation for case 1.
     * Update heights, then set new root.
     */
    void rotateWithLeftChild( AVLNode<T> * & k2 )
    {
        AVLNode<T> * k1 = k2->left;
        k2->left = k1->right;
        k1->right = k2;
        k2->height = std::max( height( k2->left ), height( k2->right ) ) + 1;
        k1->height = std::max( height( k1->left ), k2->height ) + 1;
        k2 = k1;
    }


    /**
     * Rotate binary tree node with right child.
     * For AVL trees, this is a single rotation for case 4.
     * Update heights, then set new root.
     */
    void rotateWithRightChild( AVLNode<T> * & k1 )
    {   
        AVLNode<T> * k2 = k1->right;
        k1->right = k2->left;
        k2->left = k1;
        k1->height = std::max( height( k1->left ), height( k1->right ) ) + 1;
        k2->height = std::max( height( k2->right ), k1->height ) + 1;
        k1 = k2;
    }

    /**
     * Double rotate binary tree node: first left child.
     * with its right child; then node k3 with new left child.
     * For AVL trees, this is a double rotation for case 2.
     * Update heights, then set new root.
     */
    void doubleWithLeftChild( AVLNode<T> * & k3 )
    {   
        rotateWithRightChild( k3->left );
        rotateWithLeftChild( k3 );
    }

    /**
     * Double rotate binary tree node: first right child.
     * with its left child; then node k1 with new right child.
     * For AVL trees, this is a double rotation for case 3.
     * Update heights, then set new root.
     */
    void doubleWithRightChild( AVLNode<T> * & k1 )
    {   
        rotateWithLeftChild( k1->right );
        rotateWithRightChild( k1 );
    }

    void dumpTree() {
        dumpTree(this->_root);
    }
    void dumpTree( AVLNode<T> * & t ) {
        if(t == nullptr)
            return;
        else {
            std::cout << t->val << " " << std::endl;
        }
    }

};




#endif
