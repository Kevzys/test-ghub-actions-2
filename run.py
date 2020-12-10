import requests
import xlrd

ARKG_LINK = 'https://www.ark-funds.com/auto/trades/ARK_ARKG_Trades.xls'
#ARKK_LINK = 'https://www.ark-funds.com/auto/trades/ARK_ARKK_Trades.xls'
#ARKQ_LINK = 'https://www.ark-funds.com/auto/trades/ARK_ARKQ_Trades.xls'
#ARKW_LINK = 'https://www.ark-funds.com/auto/trades/ARK_ARKW_Trades.xls'

print('Downloading excel files please wait...')

wb = xlrd.open_workbook(requests.get(ARKG_LINK))
sheets = wb.sheet_names()
print(sheets)