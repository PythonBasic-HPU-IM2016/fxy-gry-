def GameStart():
    # ��Ϸ����Surface����
    Background = pygame.image.load('GameBackground.jpg').convert()
    # ����Surface����
    Baffle = pygame.image.load('Baffle.png').convert_alpha()
    # ��Surface����
    Ball = pygame.image.load('Ball.png').convert_alpha()
    # ����λ����Ϣ
    BaffleX = 140
    BaffleY = 600
    BaffleSpeed = 1000
    BaffleXSpeed = BaffleSpeed
    BaffleYSpeed = BaffleSpeed
    BaffleMove = {K_LEFT: 0, K_RIGHT: 0, K_UP: 0, K_DOWN: 0}
    # ��λ����Ϣ
    BallX = 235
    BallY = 0
    BallSpeed = 1000.
    BallXSpeed = BallSpeed
    BallYSpeed = BallSpeed

    # ֡�ʿ���Clock����
    FPSClock = pygame.time.Clock()
    # ʱ����ʾClock����
    ProgramRunClock = pygame.time.get_ticks()
    # ʱ����ʾFont����
    RunTimeFont = pygame.font.Font('Jura-DemiBold.ttf', 24)

    # ��Ϸ���
    GameResult = ''

    while True:
        # ������Ϣ����
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key in BaffleMove:
                    BaffleMove[event.key] = 1
            elif event.type == KEYUP:
                if event.key in BaffleMove:
                    BaffleMove[event.key] = 0

        # ���Ʊ���
        Screen.blit(Background, (0, 0))

        RunTimeStr = str((pygame.time.get_ticks() - ProgramRunClock) / 1000.0)
        # print(RunTimeStr)
        # ʹ��render������ʾʱ������
        RunTimeSurface = RunTimeFont.render(RunTimeStr, True, (255, 52, 179))
        # ��ʾʱ��
        Screen.blit(RunTimeSurface, (0, 0))

        # ���ϴε���clock����ʱ��
        SecondTimePassed = FPSClock.tick(60) / 1000.0

        # ������
        Screen.blit(Ball, (BallX, BallY))

        BallX += BallXSpeed * SecondTimePassed
        BallY += BallYSpeed * SecondTimePassed

        # �ж���߽�����
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

        # ��λ�����ƶ�������
        BaffleX -= BaffleMove[K_LEFT] * BaffleXSpeed * SecondTimePassed
        BaffleX += BaffleMove[K_RIGHT] * BaffleXSpeed * SecondTimePassed
        BaffleY -= BaffleMove[K_UP] * BaffleYSpeed * SecondTimePassed
        BaffleY += BaffleMove[K_DOWN] * BaffleYSpeed * SecondTimePassed

        # �жϵ���߽�����
        if BaffleX > 500 - Baffle.get_width():
            BaffleX = 500 - Baffle.get_width()
        elif BaffleX < 0:
            BaffleX = 0
        if BaffleY > 720 - 45 - Baffle.get_height():
            BaffleY = 720 - 45 - Baffle.get_height()
        elif BaffleY < 720 - Baffle.get_height() * 3:
            BaffleY = 720 - Baffle.get_height() * 3
        # ���Ƶ���
        Screen.blit(Baffle, (BaffleX, BaffleY))

        # �ж�����ײ��������
        # �������Ͻ�
        if BallX == BaffleX - Ball.get_width() and BallY == BaffleY - Ball.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # �������½�
        elif BallX == BaffleX - Ball.get_width() and BallY == BaffleY + Baffle.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # �������Ͻ�
        elif BallX == BaffleX + Baffle.get_width() and BallY == BaffleY - Ball.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # �������½�
        elif BallX == BaffleX + Baffle.get_width() and BallY == BaffleY + Baffle.get_height():
            BallXSpeed = -BallXSpeed
            BallYSpeed = -BallYSpeed

        # �����ϱ���
        elif BallX > BaffleX and BallX < BaffleX + Baffle.get_width() and BallY > BaffleY - Ball.get_height() and BallY < BaffleY:
            BallYSpeed = -BallYSpeed
            BallY = BaffleY - Ball.get_height()

        # �����±���
        elif BallX > BaffleX and BallX < BaffleX + Baffle.get_width() and BallY < BaffleY + Baffle.get_height() and BallY > BaffleY:
            BallYSpeed = -BallYSpeed
            BallY = BaffleY + Baffle.get_height()

        # ���������
        elif BallY > BaffleY and BallY < BaffleY + Baffle.get_height() and BallX > BaffleX - Ball.get_width() and BallX < BaffleX:
            BallXSpeed = -BallXSpeed
            BallX = BaffleX

        # �����Ҳ���
        elif BallY > BaffleY and BallY < BaffleY + Baffle.get_height() and BallX > BaffleX + Baffle.get_width() - Ball.get_width() and BallX < BaffleX + Baffle.get_width():
            BallXSpeed = -BallXSpeed
            BallX = BaffleX + Baffle.get_width()


        if BallY > 720 - 45:
            GameResult = RunTimeStr

            return GameResult

        # ˢ����ʾ
        pygame.display.update()
