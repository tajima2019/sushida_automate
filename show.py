import cv2

game_window_img = cv2.imread('./img/game_window.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('game_window', game_window_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
