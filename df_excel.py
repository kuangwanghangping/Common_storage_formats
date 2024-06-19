###########这个是将df保存成excel格式
df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date")
excel_file = 'bond_data.xlsx'
df.to_excel(excel_file, index=False, startrow=1)#startrow=1的意思是第一行空着
print(f"数据已保存到 {excel_file} 文件中。")
