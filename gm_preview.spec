# -*- mode: python -*-

VERSION = '0.2.3'
block_cipher = None

a = Analysis(['src\\SHD\\gm_preview.py'],
             pathex=['C:\\Users\\ALB\\Entwicklung\\Python\\GraphicsMagick'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gm_preview_v' + VERSION,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True,
          icon='resources\\logo_shd.ico')
