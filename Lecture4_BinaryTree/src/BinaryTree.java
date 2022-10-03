public class BinaryTree {
    TreeNode root;

    public BinaryTree() {
        this.root = null;
    }

    /**
     Basic traversal: pre, in, post
     */
    public void preOrder(TreeNode root) {
        if (root == null) return;

        System.out.print(root.data + " -> ");
        preOrder(root.left);
        preOrder(root.right);
    }

    public void inOrder(TreeNode root) {
        if (root == null) return;

        inOrder(root.left);
        System.out.print(root.data + " -> ");
        inOrder(root.right);
    }

    public void postOrder(TreeNode root) {
        if (root == null) return;

        postOrder(root.left);
        postOrder(root.right);
        System.out.print(root.data + " -> ");
    }


    /**
     Size, height, diameter
     */
    public int getSize(TreeNode root) {
        if (root == null) return 0;
        return 1 + getSize(root.left) + getSize(root.right);
    }

    // The height of a tree is the depth of the deepest node in the tree
    public int getHeight(TreeNode root) {
        if (root == null) return 0;

        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);
        return leftHeight > rightHeight? 1 + leftHeight : 1 + rightHeight;
    };

//    public int getDiameter(Node root) {
//        if (root == null) return 0;
//    }

    /**
     traversal: level order, boundary order
     */
    public void levelOrder(TreeNode root) {
        if (root == null) return;
    };

    public void BoundaryOrder(TreeNode root) {};

    /**
     views: top, bottom, left, right
     */
    public void printTopLevelView(TreeNode root) {};
    public void printBottomLevelView(TreeNode root) {};
    public void printLeftView(TreeNode root) {};
    public void printRightView(TreeNode root) {};

    /**
     construct tree from in order & post order
     */
    public TreeNode constructTreeFromInOrderAndPostOrder(int[] inOrder, int[]postOrder) {};
    public TreeNode getRoot(int[] inOrder) {};

    /**
     mirror, whether same, symmetric
     */
    public void mirrorTree(TreeNode root) {};

    public boolean isSymmetric(TreeNode root) {
        return false;
    };

    public boolean areSameTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;

        return (root1.data == root2.data &&
                areSameTrees(root1.left, root2.left) &&
                areSameTrees(root1.right, root2.right));
    };
}
