def crinkly (example_path,target_path,threshold=(200,200,200,200,200,200,200,200,200)):
    import cv2
    import numpy as np
    import demo
    # 加载图片
    image1_path = example_path  # 图片路径
    image1 = cv2.imread(image1_path,cv2.IMREAD_GRAYSCALE)
    image2_path = target_path  # 图片路径
    image2 = cv2.imread(image2_path,cv2.IMREAD_GRAYSCALE)
    #如果图片加载失败，退出程序
    if image1 is None or image2 is None:
        print("无法加载图片，请检查路径！")
        exit()
    # 调整图片大小
    img1 = cv2.resize(image1, (750, 1024))  # 调整图片大小
    img2 = cv2.resize(image2, (750, 1024))  # 调整图片大小
    #...未完待续
    ans=[]
    ans.append([0,0,0,0,0])
    return ans