def GameStart():
    # 游戏背景Surface对象
    Background = pygame.image.load('GameBackground.jpg').convert()
    # 挡板Surface对象
    Baffle = pygame.image.load('Baffle.png').convert_alpha()
    # 球Surface对象
    Ball = pygame.image.load('Ball.png').convert_alpha()
    # 挡板位置信息
    BaffleX = 140
    BaffleY = 600
    BaffleSpeed = 1000
    BaffleXSpeed = BaffleSpeed
    BaffleYSpeed = BaffleSpeed
    BaffleMove = {K_LEFT: 0, K_RIGHT: 0, K_UP: 0, K_DOWN: 0}
    # 球位置信息
    BallX = 235
    BallY = 0
    BallSpeed = 1000.
    BallXSpeed = BallSpeed
    BallYSpeed = BallSpeed

    # 帧率控制Clock对象
    FPSClock = pygame.time.Clock()
    # 时间显示Clock对象
    ProgramRunClock = pygame.time.get_ticks()
    # 时间显示Font对象
    RunTimeFont = pygame.font.Font('Jura-DemiBold.ttf', 24)

    # 游戏结果
    GameResult = ''

    while True:
        # 接收信息处理
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key in BaffleMove:
                    BaffleMove[event.key] = 1
            elif event.type == KEYUP:
                if event.key in BaffleMove:
                    BaffleMove[event.key] = 0

        # 绘制背景
        Screen.blit(Background, (0, 0))

        RunTimeStr = str((pygame.time.get_ticks() - ProgramRunClock) / 1000.0)
        # print(RunTimeStr)
        # 使用render方法显示时间字体
        RunTimeSurface = RunTimeFont.render(RunTimeStr, True, (255, 52, 179))
        # 显示时间
        Screen.blit(RunTimeSurface, (0, 0))

        # 距上次调用clock对象时间
        SecondTimePassed = FPSClock.tick(60) / 1000.0

        # 绘制球
        Screen.blit(Ball, (BallX, BallY))

        BallX += BallXSpeed * SecondTimePassed
        BallY += BallYSpeed * SecondTimePassed

        # 判断球边界条件
        if BallX > 500 - Ball.get_width():
            BallXSpeed = -BallXSpeed
            BallX = 500 - Ball.get_width()
        elif BallX < 0:
            BallXSpeed = -BallXSpeed
            BallX = 0
        if BallY > 720 - Ball.get_width():
            BallYSpeed = -BallYSpeed
            BallY = 720 - Ball.get_width()
        elif BallY < 0:
            BallYSpeed = -BallYSpeed
            BallY = 0

        # 定位挡板移动后坐标
        BaffleX -= BaffleMove[K_LEFT] * BaffleXSpeed * SecondTimePassed
        BaffleX += BaffleMove[K_RIGHT] * BaffleXSpeed * SecondTimePassed
        BaffleY -= BaffleMove[K_UP] * BaffleYSpeed * SecondTimePassed
        BaffleY += BaffleMove[K_DOWN] * BaffleYSpeed * SecondTimePassed

        # 判断挡板边界条件
        if BaffleX > 500 - Baffle.get_width():
            BaffleX = 500 - Baffle.get_width()
        elif BaffleX < 0:
            BaffleX = 0
        if BaffleY > 720 - 45 - Baffle.get_height():
            BaffleY = 720 - 45 - Baffle.get_height()
        elif BaffleY < 720 - Baffle.get_height() * 3:
            BaffleY = 720 - Baffle.get_height() * 3
        # 绘制挡板
        Screen.blit(Baffle, (BaffleX, BaffleY))

        # 判断球碰撞挡板条件
        # 挡板左上角
        if BallX == BaffleX - Ball.get_width() and BallY == BaffleY - Ball.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # 挡板左下角
        elif BallX == BaffleX - Ball.get_width() and BallY == BaffleY + Baffle.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # 挡板右上角
        elif BallX == BaffleX + Baffle.get_width() and BallY == BaffleY - Ball.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # 挡板右下角
        elif BallX == BaffleX + Baffle.get_width() and BallY == BaffleY + Baffle.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # 挡板上表面
        elif BallX > BaffleX and BallX < BaffleX + Baffle.get_width() and BallY > BaffleY - Ball.get_height() and BallY < BaffleY:
            BallYSpeed = -BallYSpeed
            BallY = BaffleY - Ball.get_height()

        # 挡板下表面
        elif BallX > BaffleX and BallX < BaffleX + Baffle.get_width() and BallY < BaffleY + Baffle.get_height() and BallY > BaffleY:
            BallYSpeed = -BallYSpeed
            BallY = BaffleY + Baffle.get_height()

        # 挡板左侧面
        elif BallY > BaffleY and BallY < BaffleY + Baffle.get_height() and BallX > BaffleX - Ball.get_width() and BallX < BaffleX:
            BallXSpeed = -BallXSpeed
            BallX = BaffleX

        # 挡板右侧面
        elif BallY > BaffleY and BallY < BaffleY + Baffle.get_height() and BallX > BaffleX + Baffle.get_width() - Ball.get_width() and BallX < BaffleX + Baffle.get_width():
            BallXSpeed = -BallXSpeed
            BallX = BaffleX + Baffle.get_width()


        if BallY > 720 - 45:
            GameResult = RunTimeStr

            return GameResult

        # 刷新显示
        pygame.display.update()
