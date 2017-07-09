
public class QuadTree<Key extends Comparable<Key>, Value>  {
    private Node root;

    private class Node {
        int x, y;
        Node NW, NE, SE, SW;
        Value value;           // associated data

        Node(int x, int y, Value value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }
    }

    private static class Interval2D {
        int xmin;
        int xmax;
        int ymin;
        int ymax;

        Interval2D(int xmin, int xmax, int ymin, int ymax) {
            this.xmin = xmin;
            this.xmax = xmax;
            this.ymin = ymin;
            this.ymax = ymax;
        }

        boolean contains(int x, int y) {
            return (x >= xmin && x <= xmax && y >=ymin && y <= ymax);
        }
    }

    public void insert(int x, int y, Value value) {
        root = insert(root, x, y, value);
    }

    private Node insert(Node h, int x, int y, Value value) {
        if (h == null) return new Node(x, y, value);
        // if (eq(x, h.x) && eq(y, h.y)) h.value = value;  // duplicate
        else if ( (x < h.x) &&  (y < h.y)) h.SW = insert(h.SW, x, y, value);
        else if ( (x < h.x) && (y >= h.y)) h.NW = insert(h.NW, x, y, value);
        else if ( (x >= h.x) &&  (y < h.y)) h.SE = insert(h.SE, x, y, value);
        else if ( (x >= h.x) && (y >= h.y)) h.NE = insert(h.NE, x, y, value);
        return h;
    }


    public void query2D(Interval2D rect) {
        query2D(root, rect);
    }

    private void query2D(Node h, Interval2D rect) {
        if (h == null) return;
        int xmin = rect.xmin;
        int ymin = rect.ymin;
        int xmax = rect.xmax;
        int ymax = rect.ymax;
        if (rect.contains(h.x, h.y))
            System.out.println("    (" + h.x + ", " + h.y + ") " + h.value);
        if ( xmin < h.x &&  (ymin < h.y)) query2D(h.SW, rect);
        if ( xmin < h.x && (ymax >= h.y)) query2D(h.NW, rect);
        if ( (xmax >= h.x) &&  (ymin < h.y)) query2D(h.SE, rect);
        if ( (xmax >= h.x) && (ymax >= h.y)) query2D(h.NE, rect);
    }


    public static void main(String[] args) {
        int M = Integer.parseInt(args[0]);   // queries
        int N = Integer.parseInt(args[1]);   // points

        QuadTree<Integer, String> st = new QuadTree<Integer, String>();

        // insert N random points in the unit square
        for (int i = 0; i < N; i++) {
            Integer x = (int) (100 * Math.random());
            Integer y = (int) (100 * Math.random());
            // System.out.println("(" + x + ", " + y + ")");
            st.insert(x, y, "P" + i);
        }

        // do some range searches
        for (int i = 0; i < M; i++) {
            Integer xmin = (int) (100 * Math.random());
            Integer ymin = (int) (100 * Math.random());
            Integer xmax = xmin + (int) (10 * Math.random());
            Integer ymax = ymin + (int) (20 * Math.random());
            Interval2D rect = new Interval2D(xmin, xmax, ymin, ymax);
            System.out.println(rect + " : ");
            st.query2D(rect);
        }
    }

}

