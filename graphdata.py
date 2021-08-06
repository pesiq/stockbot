import numpy as np

# time_axis = [1627401419999, 1627401479999, 1627401539999, 1627401599999, 1627401659999, 1627401719999, 1627401779999, 1627401839999, 1627401899999, 1627401959999, 1627402019999, 1627402079999, 1627402139999, 1627402199999, 1627402259999, 1627402319999, 1627402379999, 1627402439999, 1627402499999, 1627402559999, 1627402619999, 1627402679999, 1627402739999, 1627402799999, 1627402859999, 1627402919999, 1627402979999, 1627403039999, 1627403099999, 1627403159999, 1627403219999, 1627403279999, 1627403339999, 1627403399999, 1627403459999, 1627403519999, 1627403579999, 1627403639999, 1627403699999, 1627403759999, 1627403819999, 1627403879999, 1627403939999, 1627403999999]
# values_kline_open = [38233.98, 38242.1, 38170.31, 38237.7, 38209.58, 38252.46, 38218.56, 38270.8, 38249.88, 38062.17, 38048.49, 38189.99, 38230.77, 38232.44, 38185.9, 38089.17, 38088.26, 38029.99, 37971.17, 37960.46, 37941.02, 37980.0, 37969.36, 37996.91, 37857.32, 37890.8, 37846.49, 37752.26, 37700.07, 37719.99, 37730.35, 37779.18, 37756.47, 37783.01, 37775.64, 37834.2, 37846.4, 37871.56, 37849.43, 37858.06, 37869.33, 37906.76, 37934.02, 37986.41]
# values_kline_close = [38233.98, 38231.87, 38170.33, 38237.71, 38213.7, 38255.36, 38185.08, 38284.07, 38229.54, 38074.12, 38055.51, 38173.78, 38235.65, 38208.67, 38153.54, 38093.85, 38070.01, 38026.26, 37955.56, 37961.31, 37916.66, 37986.98, 37982.64, 37982.21, 37849.99, 37891.5, 37853.62, 37779.99, 37712.3, 37748.92, 37715.06, 37764.27, 37769.52, 37774.31, 37760.62, 37813.66, 37848.99, 37869.1, 37849.42, 37854.65, 37871.2, 37912.08, 37933.88, 37983.43]
# values_kline_high = [38233.99, 38242.11, 38170.33, 38237.71, 38216.99, 38255.36, 38218.56, 38284.08, 38250.01, 38083.62, 38055.51, 38191.07, 38235.65, 38232.45, 38185.9, 38093.85, 38088.26, 38029.99, 37971.18, 37967.97, 37941.03, 37998.99, 37982.64, 37996.91, 37857.33, 37894.68, 37856.03, 37782.45, 37712.3, 37757.18, 37730.35, 37779.18, 37769.52, 37784.9, 37775.65, 37834.2, 37856.35, 37871.57, 37852.5, 37864.99, 37871.21, 37915.16, 37934.03, 37986.42]
# values_kline_low = [38233.98, 38231.86, 38170.31, 38237.7, 38209.58, 38252.45, 38185.07, 38270.8, 38224.44, 38059.88, 38040.12, 38173.78, 38230.77, 38205.97, 38153.54, 38087.56, 38070.01, 38016.64, 37955.56, 37960.45, 37916.66, 37980.0, 37969.35, 37982.21, 37841.72, 37890.8, 37846.48, 37752.26, 37700.07, 37719.99, 37711.82, 37764.27, 37756.46, 37774.31, 37756.99, 37810.75, 37846.4, 37858.13, 37843.0, 37853.46, 37869.33, 37906.76, 37922.72, 37983.43]
# values_SMA_7 = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 38225.44571428571, 38225.112857142856, 38211.368571428575, 38185.340000000004, 38179.637142857144, 38176.82142857143, 38180.19142857143, 38161.544285714284, 38142.159999999996, 38141.572857142855, 38137.39428571429, 38106.22000000001, 38067.02857142857, 38025.31285714286, 38001.51857142857, 37985.631428571425, 37973.08857142857, 37947.90714285714, 37938.75571428571, 37923.37142857142, 37903.84714285714, 37864.607142857145, 37831.218571428566, 37793.05428571429, 37780.80857142857, 37763.38285714285, 37752.05285714285, 37749.2857142857, 37763.76571428571, 37778.06142857142, 37800.06714285714, 37812.23142857143, 37824.392857142855, 37838.23428571429, 37859.87142857142, 37877.04571428571, 37896.25142857142]
# values_SMA_25 = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 38097.03599999999, 38081.90599999999, 38066.2924, 38045.276, 38026.6848, 38005.0728, 37988.2404, 37967.65840000001, 37949.44920000001, 37936.9092, 37927.23520000001, 37914.2436, 37899.581600000005, 37885.21160000001, 37873.256, 37864.35, 37858.0328, 37854.337600000006, 37855.4524]
# values_SMA_99 = []


time_axis = [1627653779999, 1627653839999, 1627653899999, 1627653959999, 1627654019999, 1627654079999, 1627654139999, 1627654199999, 1627654259999, 1627654319999, 1627654379999, 1627654439999, 1627654499999, 1627654559999, 1627654619999, 1627654679999, 1627654739999, 1627654799999, 1627654859999, 1627654919999, 1627654979999, 1627655039999, 1627655099999, 1627655159999, 1627655219999, 1627655279999, 1627655339999, 1627655399999, 1627655459999, 1627655519999, 1627655579999, 1627655639999, 1627655699999, 1627655759999, 1627655819999, 1627655879999, 1627655939999, 1627655999999, 1627656059999, 1627656119999, 1627656179999, 1627656239999, 1627656299999, 1627656359999, 1627656419999, 1627656479999, 1627656539999, 1627656599999, 1627656659999, 1627656719999, 1627656779999, 1627656839999, 1627656899999, 1627656959999, 1627657019999, 1627657079999, 1627657139999, 1627657199999, 1627657259999, 1627657319999, 1627657379999, 1627657439999, 1627657499999, 1627657559999, 1627657619999, 1627657679999, 1627657739999, 1627657799999, 1627657859999, 1627657919999, 1627657979999, 1627658039999, 1627658099999, 1627658159999, 1627658219999, 1627658279999, 1627658339999, 1627658399999, 1627658459999, 1627658519999, 1627658579999, 1627658639999, 1627658699999, 1627658759999, 1627658819999, 1627658879999, 1627658939999, 1627658999999, 1627659059999, 1627659119999, 1627659179999, 1627659239999, 1627659299999, 1627659359999, 1627659419999, 1627659479999, 1627659539999, 1627659599999, 1627659659999, 1627659719999, 1627659779999, 1627659839999, 1627659899999, 1627659959999, 1627660019999, 1627660079999, 1627660139999, 1627660199999, 1627660259999, 1627660319999, 1627660379999, 1627660439999, 1627660499999, 1627660559999, 1627660619999, 1627660679999, 1627660739999, 1627660799999, 1627660859999, 1627660919999, 1627660979999, 1627661039999, 1627661099999, 1627661159999, 1627661219999, 1627661279999, 1627661339999, 1627661399999, 1627661459999, 1627661519999, 1627661579999, 1627661639999, 1627661699999, 1627661759999, 1627661819999, 1627661879999, 1627661939999, 1627661999999, 1627662059999, 1627662119999, 1627662179999, 1627662239999, 1627662299999, 1627662359999, 1627662419999, 1627662479999, 1627662539999, 1627662599999, 1627662659999, 1627662719999, 1627662779999, 1627662839999, 1627662899999, 1627662959999, 1627663019999, 1627663079999, 1627663139999, 1627663199999, 1627663259999, 1627663319999, 1627663379999, 1627663439999, 1627663499999, 1627663559999, 1627663619999, 1627663679999, 1627663739999, 1627663799999, 1627663859999, 1627663919999, 1627663979999, 1627664039999, 1627664099999, 1627664159999, 1627664219999, 1627664279999, 1627664339999, 1627664399999, 1627664459999, 1627664519999, 1627664579999, 1627664639999, 1627664699999, 1627664759999, 1627664819999, 1627664879999, 1627664939999, 1627664999999, 1627665059999, 1627665119999, 1627665179999, 1627665239999, 1627665299999, 1627665359999, 1627665419999, 1627665479999, 1627665539999, 1627665599999, 1627665659999, 1627665719999, 1627665779999, 1627665839999, 1627665899999, 1627665959999, 1627666019999, 1627666079999, 1627666139999, 1627666199999, 1627666259999, 1627666319999, 1627666379999, 1627666439999, 1627666499999, 1627666559999, 1627666619999, 1627666679999, 1627666739999, 1627666799999, 1627666859999, 1627666919999, 1627666979999, 1627667039999, 1627667099999, 1627667159999, 1627667219999, 1627667279999, 1627667339999, 1627667399999, 1627667459999, 1627667519999, 1627667579999, 1627667639999, 1627667699999, 1627667759999, 1627667819999, 1627667879999, 1627667939999, 1627667999999, 1627668059999, 1627668119999, 1627668179999, 1627668239999, 1627668299999, 1627668359999, 1627668419999, 1627668479999, 1627668539999, 1627668599999, 1627668659999, 1627668719999, 1627668779999, 1627668839999, 1627668899999, 1627668959999, 1627669019999, 1627669079999, 1627669139999]
values_kline_open = [38893.07, 38891.82, 38900.34, 38941.24, 38934.03, 38930.91, 38959.53, 39048.37, 39078.41, 39092.95, 39126.99, 39086.78, 39052.52, 39082.06, 39034.83, 39004.82, 39030.32, 39053.09, 39007.04, 39000.26, 39031.1, 38999.03, 38997.8, 38982.98, 38985.65, 39016.32, 38983.3, 38993.64, 38999.99, 39005.39, 38976.73, 38965.31, 38972.71, 38974.03, 38964.51, 38939.49, 38935.82, 38945.56, 38943.87, 38966.93, 38959.5, 38991.85, 39010.34, 39013.07, 39042.44, 39057.68, 39024.45, 39043.24, 38972.74, 39000.5, 39030.01, 39036.69, 39005.35, 38977.44, 38981.09, 38990.08, 39000.01, 39014.98, 39023.69, 38981.81, 38960.0, 38945.91, 38950.15, 38925.56, 38893.52, 38895.4, 38937.02, 38957.44, 38958.35, 38932.86, 38909.9, 38907.74, 38963.75, 38998.99, 38984.84, 39020.0, 39022.12, 39004.9, 38981.79, 38954.99, 38987.23, 39015.26, 39040.15, 39034.68, 39039.72, 39051.27, 39024.54, 38993.76, 39034.49, 39041.71, 39030.26, 39050.0, 38996.05, 39023.82, 39023.88, 39000.0, 39023.37, 39026.95, 39039.49, 39042.9, 39060.01, 39057.1, 39038.93, 39052.27, 39043.35, 39038.42, 39031.02, 39032.99, 39042.78, 39022.01, 39017.33, 39021.46, 39021.24, 39022.72, 39065.59, 39058.2, 39063.34, 39066.28, 39072.65, 39068.39, 39022.74, 39049.56, 39012.7, 38992.59, 38966.0, 38964.77, 38963.26, 38994.0, 38989.03, 39003.62, 38987.33, 38975.45, 38970.09, 38945.98, 38887.3, 38914.15, 38971.91, 38978.43, 38978.3, 38997.49, 39005.94, 39046.91, 39088.67, 39148.44, 39118.2, 39076.69, 39072.25, 39009.62, 39005.89, 39007.62, 39051.89, 39022.98, 39038.07, 39046.07, 39024.98, 39009.99, 38995.61, 38985.34, 38979.57, 38994.64, 38990.51, 38990.57, 38989.6, 38990.46, 38962.98, 38958.82, 38949.19, 38946.27, 38979.89, 38957.68, 38949.74, 38940.22, 38951.02, 38945.58, 38947.89, 38968.72, 38936.27, 38936.53, 38909.19, 38955.29, 38939.04, 38972.89, 38945.84, 38934.49, 38960.24, 38987.6, 38982.49, 38998.99, 39000.01, 39019.99, 39011.36, 38991.98, 39000.86, 39000.96, 39000.0, 39004.52, 39008.68, 39010.45, 39033.0, 38962.93, 38960.24, 38971.35, 38980.85, 38987.78, 38983.1, 38960.0, 38933.68, 38986.83, 39017.75, 39028.19, 39020.0, 38997.74, 38994.1, 38978.58, 38985.18, 38978.57, 38971.5, 38981.88, 38994.98, 39002.65, 39003.17, 38994.62, 39012.0, 39012.87, 38998.45, 38999.69, 39003.56, 39029.99, 39038.26, 39049.16, 39024.32, 39002.38, 38999.02, 38998.02, 38999.99, 38998.36, 39002.59, 38999.78, 39018.96, 39015.83, 38991.39, 39002.97, 39016.37, 39023.18, 38998.12, 38996.05, 38972.06, 38912.72, 38939.78, 38962.92, 38966.3, 38950.05, 38960.61, 39036.81, 39039.0, 39039.14, 39029.91]
values_kline_close = [38891.13, 38895.46, 38900.72, 38927.81, 38932.17, 38930.91, 38970.0, 39048.41, 39078.42, 39088.35, 39127.34, 39085.8, 39067.84, 39079.96, 39034.88, 39008.71, 39025.01, 39065.23, 39003.85, 39000.27, 39031.85, 38999.04, 38997.79, 38981.31, 38985.66, 39016.33, 38990.78, 38993.64, 38998.71, 39004.01, 38976.56, 38972.78, 38972.71, 38974.49, 38963.55, 38939.97, 38934.08, 38941.07, 38946.13, 38966.64, 38956.82, 38991.95, 39010.12, 39013.08, 39042.43, 39056.75, 39024.45, 39043.25, 38972.74, 39000.51, 39034.94, 39036.69, 39000.8, 38970.62, 38981.09, 38988.12, 39000.0, 39013.0, 39017.25, 38984.46, 38959.99, 38941.87, 38950.16, 38922.73, 38893.51, 38895.4, 38937.01, 38957.43, 38962.18, 38932.85, 38907.73, 38905.08, 38963.75, 38975.01, 38986.62, 39019.99, 39022.18, 39001.08, 38980.99, 38964.98, 38987.22, 39015.24, 39040.16, 39034.69, 39040.02, 39046.25, 39026.48, 38991.94, 39026.34, 39034.19, 39040.01, 39038.53, 38998.47, 39018.09, 39023.89, 39005.06, 39028.37, 39021.98, 39039.48, 39044.52, 39060.0, 39057.09, 39035.02, 39052.27, 39046.72, 39038.0, 39031.02, 39032.9, 39039.12, 39023.01, 39015.27, 39022.87, 39021.24, 39023.73, 39061.03, 39058.2, 39063.33, 39066.28, 39074.61, 39068.4, 39022.73, 39049.6, 39009.15, 38992.58, 38966.01, 38959.93, 38963.56, 38987.94, 38989.02, 39007.05, 38985.01, 38983.0, 38970.08, 38945.98, 38899.99, 38918.94, 38975.11, 38978.43, 38984.89, 38999.11, 39007.89, 39041.84, 39100.59, 39152.75, 39115.48, 39076.69, 39072.26, 39007.91, 39009.82, 39001.97, 39045.0, 39038.05, 39039.96, 39046.07, 39025.68, 39009.99, 38995.62, 38985.34, 38983.21, 38994.63, 38993.17, 38999.99, 38985.21, 38981.6, 38962.95, 38959.92, 38949.17, 38962.96, 38979.89, 38955.74, 38944.89, 38940.23, 38951.02, 38941.58, 38947.89, 38973.99, 38936.28, 38940.31, 38909.19, 38956.66, 38939.03, 38972.52, 38945.83, 38934.49, 38960.23, 38987.6, 38982.49, 38997.01, 39000.01, 39014.0, 39010.05, 38991.98, 39003.17, 39000.96, 39000.01, 39005.33, 39010.03, 39010.45, 39018.89, 38964.68, 38961.23, 38967.7, 38980.85, 38978.29, 38983.09, 38960.0, 38939.45, 38991.99, 39015.79, 39037.32, 39019.99, 38992.07, 38985.7, 38974.16, 38985.18, 38975.56, 38971.5, 38968.72, 38999.0, 39004.04, 39005.18, 38996.99, 39012.0, 39014.85, 38997.04, 38999.69, 39003.55, 39026.25, 39035.47, 39049.85, 39024.32, 39002.38, 38997.6, 38998.03, 39000.83, 38998.36, 39001.34, 38999.78, 39017.33, 39000.0, 38993.74, 39002.98, 39016.37, 39026.81, 38998.13, 38995.79, 38970.01, 38911.01, 38937.41, 38962.95, 38966.3, 38950.06, 38961.03, 39030.36, 39038.99, 39039.56, 39074.75]
values_kline_high = [38893.08, 38895.47, 38901.11, 38941.24, 38934.04, 38930.92, 38974.05, 39053.49, 39078.51, 39097.9, 39127.35, 39086.78, 39073.72, 39085.27, 39034.88, 39008.72, 39030.32, 39075.01, 39007.04, 39000.27, 39031.85, 38999.04, 38997.8, 38982.99, 38985.66, 39016.33, 38990.78, 38993.65, 38999.99, 39005.39, 38976.73, 38974.03, 38972.72, 38977.55, 38965.58, 38942.73, 38935.82, 38945.56, 38949.99, 38967.01, 38959.51, 38991.96, 39013.65, 39013.08, 39042.45, 39057.68, 39024.46, 39043.25, 38972.75, 39000.51, 39034.94, 39036.69, 39005.35, 38977.44, 38981.09, 38990.09, 39000.01, 39014.99, 39023.69, 38984.46, 38960.0, 38945.92, 38950.16, 38925.56, 38895.39, 38895.41, 38937.02, 38961.31, 38962.36, 38932.86, 38912.25, 38907.75, 38963.76, 38998.99, 38992.08, 39020.0, 39025.49, 39004.91, 38981.79, 38964.98, 38987.23, 39017.28, 39040.16, 39034.69, 39040.02, 39051.27, 39030.0, 38993.76, 39034.49, 39041.71, 39040.02, 39050.0, 39002.24, 39023.82, 39023.9, 39010.15, 39028.53, 39026.95, 39039.49, 39044.52, 39060.01, 39057.1, 39038.93, 39052.28, 39046.72, 39038.42, 39031.03, 39033.0, 39042.79, 39026.12, 39019.67, 39022.88, 39021.25, 39023.74, 39065.94, 39058.2, 39063.34, 39066.28, 39076.65, 39072.66, 39022.74, 39049.61, 39012.71, 38994.69, 38966.01, 38964.78, 38963.56, 38994.0, 38989.03, 39007.05, 38989.55, 38983.0, 38973.03, 38945.99, 38900.0, 38918.94, 38975.14, 38978.44, 38984.89, 38999.11, 39007.89, 39049.99, 39106.22, 39152.75, 39118.2, 39076.69, 39072.26, 39009.62, 39020.32, 39007.63, 39051.89, 39038.06, 39044.99, 39046.08, 39025.68, 39010.0, 38995.62, 38987.8, 38983.22, 38994.64, 38993.18, 39000.0, 38989.61, 38990.46, 38963.98, 38959.93, 38949.19, 38962.96, 38979.89, 38957.68, 38949.74, 38940.23, 38951.03, 38945.58, 38947.89, 38979.63, 38936.28, 38940.32, 38909.2, 38956.67, 38939.04, 38972.9, 38945.84, 38934.49, 38960.24, 38987.61, 38982.5, 38999.0, 39000.01, 39020.0, 39011.36, 38991.99, 39004.81, 39000.96, 39000.01, 39005.33, 39012.25, 39010.46, 39033.0, 38964.68, 38961.23, 38971.35, 38980.85, 38987.79, 38983.1, 38960.01, 38943.19, 38994.22, 39017.75, 39037.32, 39020.0, 38997.74, 38994.1, 38978.59, 38985.18, 38978.58, 38971.51, 38981.88, 38999.0, 39004.04, 39005.18, 38997.0, 39012.0, 39016.63, 38998.46, 38999.69, 39003.56, 39030.0, 39038.26, 39049.86, 39024.33, 39002.38, 38999.02, 38999.09, 39000.83, 38998.37, 39002.6, 38999.78, 39019.58, 39015.83, 38993.75, 39002.98, 39016.37, 39026.82, 38998.13, 38996.06, 38972.06, 38912.72, 38939.78, 38962.96, 38966.3, 38950.06, 38968.66, 39036.81, 39039.0, 39042.31, 39074.78]
values_kline_low = [38889.28, 38891.81, 38900.34, 38921.67, 38932.16, 38930.91, 38959.49, 39045.08, 39075.21, 39084.91, 39124.28, 39085.8, 39052.51, 39079.96, 39034.83, 39004.81, 39025.01, 39053.08, 39001.92, 38998.11, 39031.1, 38999.03, 38997.79, 38981.31, 38985.65, 39016.32, 38983.3, 38993.64, 38998.7, 39004.0, 38975.0, 38965.31, 38972.71, 38974.03, 38961.32, 38939.49, 38934.08, 38941.05, 38943.86, 38966.64, 38954.89, 38991.84, 39010.11, 39013.07, 39042.43, 39056.75, 39024.45, 39043.24, 38972.74, 39000.5, 39027.43, 39036.68, 39000.8, 38970.61, 38981.09, 38982.36, 39000.0, 39013.0, 39015.48, 38979.94, 38955.35, 38941.21, 38950.15, 38917.67, 38886.33, 38895.4, 38937.01, 38957.43, 38958.35, 38932.85, 38907.73, 38905.08, 38963.75, 38975.0, 38984.84, 39019.99, 39022.11, 39001.08, 38980.98, 38952.02, 38987.22, 39015.24, 39037.87, 39031.71, 39039.71, 39046.12, 39024.53, 38991.94, 39026.34, 39034.19, 39030.26, 39036.16, 38996.04, 39016.12, 39023.87, 39000.0, 39023.36, 39018.71, 39039.48, 39042.9, 39060.0, 39057.09, 39035.01, 39052.27, 39043.35, 39038.0, 39031.02, 39028.03, 39039.12, 39022.0, 39015.27, 39021.44, 39021.24, 39022.71, 39061.03, 39058.19, 39063.33, 39066.28, 39072.65, 39068.39, 39022.73, 39049.56, 39005.7, 38990.83, 38966.0, 38957.31, 38961.01, 38987.93, 38989.02, 39003.62, 38983.68, 38975.44, 38969.02, 38945.98, 38887.3, 38914.13, 38971.91, 38978.43, 38978.29, 38997.48, 39003.91, 39041.84, 39088.66, 39148.44, 39115.47, 39076.68, 39072.25, 39007.91, 39005.89, 38999.09, 39039.8, 39022.98, 39038.07, 39046.07, 39024.98, 39009.99, 38995.61, 38985.33, 38979.57, 38992.37, 38990.51, 38990.57, 38985.21, 38981.6, 38962.95, 38958.82, 38947.54, 38946.27, 38979.88, 38955.74, 38944.88, 38940.22, 38951.02, 38941.58, 38947.88, 38968.71, 38936.27, 38936.53, 38909.19, 38955.29, 38939.03, 38972.51, 38945.83, 38934.48, 38960.23, 38987.6, 38982.49, 38997.01, 39000.0, 39013.99, 39010.04, 38991.97, 39000.85, 39000.95, 39000.0, 39004.52, 39008.67, 39010.45, 39018.88, 38962.93, 38960.23, 38960.96, 38980.84, 38977.92, 38983.09, 38960.0, 38933.67, 38986.83, 39012.8, 39028.19, 39019.98, 38986.83, 38985.69, 38974.14, 38985.17, 38974.03, 38971.5, 38968.71, 38994.98, 39002.51, 39003.16, 38994.62, 39011.99, 39012.86, 38993.18, 38999.68, 39003.55, 39026.24, 39033.07, 39049.16, 39019.99, 39002.37, 38997.44, 38998.01, 38999.99, 38997.45, 39001.34, 38999.77, 39017.33, 39000.0, 38991.39, 39002.97, 39016.37, 39023.17, 38998.12, 38995.79, 38970.01, 38911.01, 38937.36, 38962.91, 38966.29, 38950.05, 38960.61, 39030.35, 39038.99, 39039.14, 39029.91]
values_SMA_7 = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 38943.64, 38969.777142857136, 38996.58142857143, 39025.08571428572, 39047.032857142854, 39066.59428571429, 39082.30285714286, 39080.369999999995, 39070.41142857143, 39061.36285714286, 39052.49, 39040.782857142854, 39031.130000000005, 39024.25714285714, 39019.137142857144, 39017.57714285714, 39011.33428571429, 38999.967142857146, 39001.75, 39000.39428571429, 38994.93571428571, 38994.88857142858, 38995.77714285715, 38995.09857142856, 38993.258571428574, 38987.027142857136, 38984.7, 38980.40142857143, 38972.01, 38962.020000000004, 38956.95, 38953.142857142855, 38952.275714285715, 38949.75142857143, 38953.80857142858, 38963.83000000001, 38975.11571428571, 38989.59571428572, 39005.39857142857, 39013.65714285715, 39026.00428571429, 39023.26, 39021.887142857144, 39025.01, 39024.19, 39016.19714285714, 39008.50714285715, 38999.62714285714, 39001.82428571429, 39001.75142857143, 38998.61714285715, 38995.840000000004, 38993.50571428571, 38991.98714285715, 38986.38428571429, 38980.96142857143, 38969.922857142854, 38952.852857142854, 38935.44571428571, 38928.66714285715, 38928.30142857144, 38931.20285714286, 38928.729999999996, 38926.58714285714, 38928.24, 38938.00428571428, 38943.43285714286, 38947.60285714286, 38955.861428571436, 38968.62285714286, 38981.95857142857, 38992.80285714286, 38992.97857142857, 38994.72285714286, 38998.811428571425, 39001.69285714285, 39003.479999999996, 39009.04285714286, 39018.36571428571, 39027.15142857143, 39027.82571428572, 39029.41142857143, 39028.55857142858, 39029.31857142858, 39029.10571428571, 39022.280000000006, 39021.08142857143, 39025.64571428572, 39022.60571428571, 39021.77428571428, 39019.19857142858, 39019.33428571429, 39025.91285714286, 39031.9, 39036.642857142855, 39040.92285714286, 39044.33714285714, 39047.87142857142, 39047.659999999996, 39045.73142857143, 39041.86, 39039.29285714286, 39037.57714285714, 39032.29142857143, 39028.88428571428, 39026.49, 39025.44857142858, 39029.467142857146, 39032.19285714285, 39037.95285714285, 39045.24, 39052.631428571425, 39059.368571428575, 39059.22571428573, 39057.59285714286, 39050.58571428571, 39040.47857142857, 39026.154285714285, 39009.77142857143, 38994.794285714284, 38989.82428571429, 38981.17, 38980.87, 38979.788571428566, 38982.21571428572, 38983.66571428572, 38981.15428571428, 38968.590000000004, 38958.57857142857, 38954.01571428572, 38953.07571428572, 38953.345714285715, 38957.49285714285, 38966.33714285714, 38986.60142857143, 39012.55142857142, 39037.92857142857, 39057.50714285714, 39070.62142857142, 39081.07142857143, 39081.07428571429, 39076.5, 39062.41142857143, 39047.01857142857, 39035.95714285714, 39030.71000000001, 39026.96857142857, 39029.50714285714, 39029.53142857143, 39028.624285714286, 39020.10142857143, 39012.26714285714, 39005.79142857143, 38998.23428571428, 38994.56428571429, 38991.02428571428, 38989.021428571425, 38985.822857142855, 38982.49571428571, 38976.00142857142, 38971.68571428571, 38968.81428571429, 38964.60428571428, 38959.36, 38956.114285714284, 38954.84285714286, 38953.75857142858, 38951.60571428571, 38950.76285714286, 38947.98285714286, 38947.32857142857, 38942.89428571429, 38943.700000000004, 38943.33571428571, 38946.85428571428, 38942.83142857143, 38942.57571428572, 38945.42142857143, 38956.62285714286, 38960.31285714286, 38968.59571428572, 38972.52285714286, 38982.26142857143, 38993.055714285714, 38997.59142857143, 38999.815714285716, 39002.454285714295, 39002.88285714285, 39003.642857142855, 39003.07571428572, 39003.13285714285, 39006.97714285715, 39001.478571428575, 38995.80285714286, 38991.18714285714, 38987.689999999995, 38983.15571428572, 38979.24714285714, 38970.83428571429, 38967.229999999996, 38971.624285714286, 38978.49428571428, 38986.561428571425, 38992.51857142857, 38993.80142857142, 38997.47285714286, 39002.43142857143, 39001.458571428564, 38995.71142857143, 38986.30857142857, 38978.98428571429, 38979.974285714285, 38982.59428571429, 38987.025714285715, 38988.712857142855, 38993.91857142857, 39000.111428571436, 39004.15714285714, 39004.25571428571, 39004.18571428571, 39007.19571428571, 39012.692857142865, 39018.1, 39019.45285714285, 39020.21571428572, 39019.91714285714, 39019.12857142858, 39015.49714285714, 39010.19571428571, 39003.26571428571, 38999.76, 39001.89571428572, 39002.23857142858, 39001.625714285714, 39001.932857142856, 39004.50571428571, 39008.14428571429, 39007.90857142857, 39004.83142857143, 39000.54714285715, 38988.72857142857, 38979.361428571436, 38971.729999999996, 38963.08571428572, 38956.21857142857, 38951.25285714286, 38959.874285714286, 38978.15714285714, 38992.75, 39008.72142857143]
values_SMA_25 = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 39011.3248, 39015.13760000001, 39018.854400000004, 39021.6904, 39024.564, 39026.38999999999, 39026.5012, 39023.473199999986, 39019.31599999999, 39014.32399999999, 39006.8292, 39000.7604, 38995.6896, 38990.3364, 38987.60680000001, 38985.5312, 38984.20880000001, 38982.004400000005, 38982.3736, 38984.060000000005, 38985.056000000004, 38986.072400000005, 38987.8908, 38987.548, 38988.142, 38988.8864, 38990.722799999996, 38991.0092, 38989.885599999994, 38988.9688, 38989.4312, 38990.51999999999, 38992.13159999999, 38993.84199999999, 38994.67839999999, 38995.47919999999, 38995.790799999995, 38996.15439999999, 38995.21839999999, 38992.29319999999, 38989.83639999999, 38987.6388, 38985.5312, 38983.4952, 38979.112, 38973.1512, 38968.376399999994, 38965.19639999999, 38965.2872, 38964.7316, 38964.1336, 38963.553199999995, 38963.564399999996, 38963.979199999994, 38963.3348, 38963.2988, 38963.9084, 38964.99480000001, 38965.6924, 38967.914800000006, 38971.3652, 38974.7496, 38976.4208, 38980.5652, 38986.1924, 38991.976800000004, 38996.037599999996, 38997.6792, 38999.91559999999, 39003.557199999996, 39007.450399999994, 39012.382, 39014.7112, 39017.29, 39019.606, 39021.2064, 39022.60279999999, 39023.960399999996, 39026.81159999999, 39030.08119999999, 39032.1124, 39032.7436, 39032.453199999996, 39032.6304, 39031.95, 39030.7108, 39030.566399999996, 39031.738399999995, 39031.63399999999, 39032.707599999994, 39033.43519999999, 39034.4272, 39037.1396, 39039.400400000006, 39041.1808, 39041.8876, 39042.7368, 39042.2236, 39040.3476, 39037.207200000004, 39033.2044, 39029.463200000006, 39027.58, 39025.05, 39023.4632, 39021.3436, 39019.4228, 39016.91, 39013.1844, 39008.2636, 39004.41039999999, 39002.5, 39000.787599999996, 38999.234, 38996.7572, 38994.7448, 38993.885200000004, 38995.257600000004, 38998.38320000001, 39000.26640000001, 39002.42480000001, 39003.33120000001, 39003.2816, 39003.97120000001, 39005.409600000006, 39008.8124, 39011.792, 39013.8728, 39016.1548, 39016.899999999994, 39017.89919999999, 39018.404, 39019.01439999999, 39020.503600000004, 39024.2892, 39027.25839999999, 39028.253600000004, 39028.5248, 39028.39319999999, 39026.94679999999, 39025.028, 39021.3212, 39015.816, 39008.901600000005, 39002.512, 38997.24, 38991.95879999999, 38989.68319999999, 38986.9536, 38984.7904, 38981.95, 38977.879199999996, 38973.89319999999, 38968.418, 38965.657199999994, 38962.8188, 38961.894799999995, 38960.3144, 38958.3656, 38956.9896, 38956.7668, 38956.0668, 38956.5388, 38957.275200000004, 38959.317200000005, 38961.322400000005, 38963.0348, 38964.643200000006, 38965.486000000004, 38967.2568, 38969.6744, 38972.466400000005, 38974.8436, 38977.936, 38978.60760000001, 38978.0972, 38979.35400000001, 38980.9756, 38983.7396, 38984.796800000004, 38985.63560000001, 38984.3128, 38986.1592, 38989.411199999995, 38992.4948, 38993.7904, 38994.173599999995, 38993.7212, 38992.6872, 38991.5344, 38990.1548, 38989.3356, 38987.957599999994, 38987.879199999996, 38988.0404, 38988.0344, 38987.5128, 38987.574799999995, 38987.413199999995, 38988.707599999994, 38990.24599999999, 38991.67999999999, 38993.49599999999, 38995.7832, 38998.45359999999, 39001.026399999995, 39003.5436, 39003.768, 39003.0576, 39001.598000000005, 39000.7328, 39001.1036, 39001.666800000006, 39003.39360000001, 39003.98640000001, 39004.7136, 39005.9728, 39007.878800000006, 39008.991200000004, 39008.754799999995, 39008.379199999996, 39007.299999999996, 39003.2604, 39000.16279999999, 38998.79919999999, 38997.463599999995, 38995.32399999999, 38992.71519999999, 38992.51079999999, 38992.07639999999, 38992.685999999994, 38995.580799999996]
values_SMA_99 = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 38995.74525252525, 38997.40727272728, 38998.986767676775, 39000.0696969697, 39001.282828282834, 39002.45262626263, 39003.13949494949, 39002.96383838384, 39002.50404040404, 39002.006767676765, 39000.95292929293, 39000.240505050504, 38999.78626262626, 38999.193131313135, 38999.08050505051, 38999.60898989899, 38999.944242424244, 38999.92505050506, 39000.555656565666, 39001.306565656574, 39001.67575757576, 39001.91505050506, 39002.43838383839, 39002.7195959596, 39002.7894949495, 39002.28121212121, 39001.96959595961, 39001.665757575756, 39001.55696969697, 39001.40555555556, 39001.71353535354, 39001.83707070708, 39001.94101010103, 39001.89646464648, 39001.718989899004, 39001.31515151517, 39001.162222222236, 39001.50606060608, 39001.832323232346, 39002.01666666669, 39002.443838383864, 39002.60484848487, 39002.925252525274, 39003.809191919216, 39004.92353535355, 39005.51676767678, 39006.04444444446, 39006.33747474749, 39006.69272727274, 39006.78676767678, 39006.45373737375, 39006.53767676769, 39006.913939393955, 39007.614343434354, 39008.270707070726, 39008.65010101011, 39008.75101010102, 39008.57545454547, 39008.25313131315, 39008.24050505052, 39008.59040404041, 39009.1085858586, 39009.61191919193, 39010.24303030304, 39011.13282828284, 39011.815151515155, 39012.04656565658, 39011.96313131315, 39011.97101010102, 39012.44616161617, 39012.931111111124, 39013.333232323246, 39013.09565656566, 39012.85333333334, 39012.398383838394, 39011.6701010101, 39011.183333333334, 39010.528787878786, 39010.11787878788, 39009.55434343434, 39009.245656565654, 39008.47585858586, 39007.79262626262, 39006.895050505045, 39005.82909090908, 39004.9602020202, 39004.56747474747, 39004.47202020201, 39004.17575757575, 39003.8305050505, 39003.567777777775, 39003.2801010101, 39003.214545454546, 39003.06383838384, 39002.83222222222, 39002.78121212121, 39002.54848484848, 39002.42777777777, 39002.13454545454, 39001.875656565644, 39000.91282828282, 38999.944545454535, 38999.264545454535, 38998.54313131312, 38997.85191919191, 38997.29727272726, 38996.57989898988, 38995.635959595944, 38995.15989898988, 38995.08696969696, 38995.30969696969, 38995.280606060594, 38994.98595959594, 38994.60181818181, 38993.72434343433, 38992.98676767675, 38992.10020202019, 38991.14282828281, 38990.07323232323, 38989.37222222222, 38989.18343434343, 38988.734747474744, 38988.61191919191, 38988.80808080808, 38989.30141414142, 38989.676262626264, 38990.04121212121, 38990.19888888888, 38990.57494949495, 38990.862020202025, 38991.516969696975, 38991.93434343435, 38992.26060606061, 38992.78202020203, 38993.772323232326, 38994.5994949495, 38994.83434343435, 38995.065757575765, 38995.21616161617, 38995.40020202021, 38995.32050505051, 38994.83464646465, 38993.848686868696, 38992.471111111125, 38991.57545454546, 38990.781919191926, 38990.0094949495, 38989.62666666667, 38988.62858585859, 38987.97646464646, 38987.14767676768, 38986.42292929293, 38985.514848484854, 38984.655858585866, 38984.70313131314, 38984.99606060607, 38985.439898989905, 38986.34303030304]
