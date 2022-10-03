public class Main {
    public static void main(String[] args) {

        BinaryTree binaryTree1 = new BinaryTree();
        TreeNode root1 = new TreeNode(1);
        binaryTree1.root = root1;
        root1.left = new TreeNode(2);
        root1.right = new TreeNode(3);
        root1.left.left = new TreeNode(4);
        root1.left.right = new TreeNode(5);
        root1.right.left = new TreeNode(6);
        root1.right.right = new TreeNode(7);
        root1.left.left.left = new TreeNode(8);

//                           1
//                        /     \
//                      2         3
//                    /  \      /  \
//                   4    5     6    7
//                 /
//                8

        System.out.println("Pre order traversal");
        binaryTree1.preOrder(root1);
        System.out.println("\nIn order traversal");
        binaryTree1.inOrder(root1);
        System.out.println("\nPost order traversal");
        binaryTree1.postOrder(root1);

        System.out.println("\nTree size: " + binaryTree1.getSize(root1));
        System.out.println("Tree height: " + binaryTree1.getHeight(root1));
        // System.out.println("\nTree diameter: " + binaryTree1.getDiameter(root1));

    }


}
