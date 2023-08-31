class Solution:
    def floodFill(self, image, sr, sc, color):
        # Base Case:
        if image[sr][sc] == color:
            return image
        else:
            c = image[sr][sc]
            image[sr][sc] = color
            # top
            if sr != 0:
                if image[sr-1][sc] == c:
                    self.floodFill(image, sr=sr-1, sc=sc, color=color)

            # left
            if sc != 0:
                if image[sr][sc-1] == c:
                    self.floodFill(image, sr=sr, sc=sc - 1, color=color)

            # right
            if sc != len(image[0])-1:
                if image[sr][sc + 1] == c:
                    self.floodFill(image, sr=sr, sc=1 + sc, color=color)

            # bottom
            if sr != len(image)-1:
                if image[sr+1][sc] == c:
                    self.floodFill(image, sr=1+sr, sc=sc, color=color)
        return image
