import qrcode

s = 'https://www.bing.com/search?q=google+chrome&form=ANNTH1&refig=1d0ac8a81eb243de90353fa1e395c5f7&pc=NMTS&pq=goo&pqlth=3&assgl=13&sgcn=google+chrome&qs=MB&smvpcn=0&swbcn=10&sctcn=0&sc=10-3&sp=3&ghc=0&cvid=1d0ac8a81eb243de90353fa1e395c5f7&clckatsg=1&hsmssg=0'


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  
    border=4
)

qr.add_data(s)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("googlechrome.png")
img.show()




# import pyqrcode 
# from pyqrcode import QRCode 
  
# # String which represent the QR code 
# s = 'https://www.bing.com/search?q=google+chrome&form=ANNTH1&refig=1d0ac8a81eb243de90353fa1e395c5f7&pc=NMTS&pq=goo&pqlth=3&assgl=13&sgcn=google+chrome&qs=MB&smvpcn=0&swbcn=10&sctcn=0&sc=10-3&sp=3&ghc=0&cvid=1d0ac8a81eb243de90353fa1e395c5f7&clckatsg=1&hsmssg=0'
  
# # Generate QR code 
# url = pyqrcode.create(s) 
  
# # Create and save the png file naming "myqr.png" 
# url.svg("googlec.svg", scale = 10)

