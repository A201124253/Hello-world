# -*- mode: python -*-

block_cipher = None


a = Analysis(['10-\xe5\xad\xa6\xe7\x94\x9f\xe7\xae\xa1\xe7\x90\x86\xe7\xb3\xbb\xe7\xbb\x9f-\xe6\x96\x87\xe4\xbb\xb6\xe7\x89\x88.py'],
             pathex=['/home/jimmy/Hello-world/05-\xe6\x96\x87\xe4\xbb\xb6\xe6\x93\x8d\xe4\xbd\x9c'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='10-学生管理系统-文件版',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
