role_list = {
    # admin 管理员权限
    'admin': [],
    # 游客权限
    'tourist': [
        ('操作', 'RBAC')
        # 第一位表示可以读取记录 r
        # 第二位表示可以新建记录 a
        # 第三位表示可以更新记录 u
        # 第四位表示可以删除记录 d
    ]
}