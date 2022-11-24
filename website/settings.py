import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
IMAGE_UPLOADS = os.environ.get('IMAGE_UPLOADS_PATH')
IMAGE_EXTENSIONS = os.environ.get('IMAGE_EXTENSIONS')
IMAGE_UPLOAD_API = os.environ.get('IMAGE_UPLOAD_API')

if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

IMAGES = ['1F301.png', '1F302.png', '1F305.png', '1F308.png', '1F30A.png', '1F320.png', '1F324.png', '1F329.png',
          '1F330.png', '1F33D.png', '1F345.png', '1F347.png', '1F34E.png', '1F352.png', '1F36D.png', '1F372.png',
          '1F376.png', '1F377.png', '1F381.png', '1F383.png', '1F384.png', '1F389.png', '1F38B.png', '1F38D.png',
          '1F390.png', '1F39B.png', '1F39E.png', '1F3A0.png', '1F3A1.png', '1F3A2.png', '1F3AA.png', '1F3AD.png',
          '1F3B1.png', '1F3B2.png', '1F3B3.png', '1F3BB.png', '1F3BE.png', '1F3C0.png', '1F3C5.png', '1F3C6.png',
          '1F3C8.png', '1F3CD.png', '1F3CE.png', '1F3D2.png', '1F3D4.png', '1F3D5.png', '1F3D6.png', '1F3D7.png',
          '1F3D8.png', '1F3DA.png', '1F3DC.png', '1F3DD.png', '1F3DE.png', '1F3DF.png', '1F3E0.png', '1F3E3.png',
          '1F3E6.png', '1F3E8.png', '1F3EF.png', '1F3F0.png', '1F3F5.png', '1F3F7.png', '1F405.png', '1F406.png',
          '1F408-200D-2B1B.png', '1F409.png', '1F40D.png', '1F414.png', '1F419.png', '1F41F.png', '1F422.png',
          '1F42B.png', '1F42C.png', '1F42D.png', '1F42E.png', '1F431-200D-1F4BB.png', '1F43B-200D-2744-FE0F.png',
          '1F43B.png', '1F43C.png', '1F43F.png', '1F451.png', '1F45A.png', '1F45B.png', '1F45C.png', '1F45D.png',
          '1F45E.png', '1F45F.png', '1F461.png', '1F462.png', '1F479.png', '1F484.png', '1F48D.png', '1F48E.png',
          '1F4A7.png', '1F4BA.png', '1F4E0.png', '1F4E2.png', '1F4E3.png', '1F4E8.png', '1F4EC.png', '1F4ED.png',
          '1F4EF.png', '1F4F1.png', '1F4F7.png', '1F4F8.png', '1F4FA.png', '1F4FB.png', '1F4FD.png', '1F50A.png',
          '1F50C.png', '1F514.png', '1F525.png', '1F526.png', '1F52C.png', '1F52E.png', '1F531.png', '1F56F.png',
          '1F579.png', '1F5A5.png', '1F5A8.png', '1F5B1.png', '1F5B2.png', '1F5BC.png', '1F5F3.png', '1F5FB.png',
          '1F5FC.png', '1F5FD.png', '1F681.png', '1F684.png', '1F687.png', '1F68C.png', '1F692.png', '1F696.png',
          '1F697.png', '1F699.png', '1F69C.png', '1F69D.png',
          '1F6A0.png', '1F6A2.png', '1F6CB.png', '1F6CD.png', '1F6D5.png', '1F6E4.png', '1F6E9.png', '1F6EC.png',
          '1F6F0.png', '1F6F3.png', '1F6F5.png', '1F6F6.png', '1F6F7.png', '1F6F8.png', '1F6FA.png', '1F6FB.png',
          '1F93F.png', '1F947.png', '1F949.png', '1F94A.png', '1F94B.png', '1F94C.png', '1F94D.png', '1F94E.png',
          '1F94F.png', '1F961.png', '1F963.png', '1F967.png', '1F968.png', '1F969.png', '1F96F.png', '1F97B.png',
          '1F97C.png', '1F980.png', '1F984.png', '1F989.png', '1F98F.png', '1F990.png', '1F991.png', '1F992.png',
          '1F993.png', '1F994.png', '1F99A.png', '1F99C.png', '1F99F.png', '1F9A0.png', '1F9A1.png', '1F9A2.png',
          '1F9A6.png', '1F9A7.png', '1F9A9.png', '1F9AE.png', '1F9BA.png', '1F9C1.png', '1F9C6.png', '1F9CB.png',
          '1F9DC-1F3FF.png', '1F9E2.png', '1F9E9.png', '1F9F3.png', '1F9F5.png', '1F9F6.png', '1F9F7.png', '1F9F8.png',
          '1FA70.png', '1FA73.png', '1FA74.png', '1FA83.png', '1FA85.png', '1FA86.png', '1FA97.png', '1FA98.png',
          '1FA9E.png',
          '1FAB4.png', '1FAB6.png', '1FAD1.png', '1FAD3.png', '1FAD4.png', '1FAD5.png', '1FAD6.png', '2328.png',
          '23F2.png', '2602.png', '2603.png', '2615.png', '26A1.png', '26BD.png', '26BE.png', '26C4.png', '26EA.png',
          '26F2.png', '26F4.png', '26FD.png', '2712.png', 'E000.png', 'E001.png', 'E002.png', 'E006.png', 'E008.png',
          'E009.png', 'E010.png', 'E048.png', 'E049.png', 'E0C0.png', 'E0C3.png', 'E0C4.png', 'E0C5.png', 'E0C6.png',
          'E149.png', 'E150.png', 'E151.png', 'E152.png', 'E153.png', 'E154.png', 'E155.png', 'E156.png', 'E182.png',
          'E1C8.png', 'E1D1.png', 'E1D2.png', 'E1D7.png', 'E200.png', 'E20B.png', 'E20C.png', 'E20D.png', 'E242.png',
          'E2CD.png', 'E2D1.png', 'E30E.png', 'E31B.png', 'E343.png', 'E344.png', 'E345.png',
          ]
