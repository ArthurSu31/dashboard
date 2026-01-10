# streamlit run dashboard.py


import streamlit as st
from PIL import Image
import numpy as np
Image.MAX_IMAGE_PIXELS = None

#import psutil
#import os

#process = psutil.Process(os.getpid())

#def log_mem(tag):
#    mem = process.memory_info().rss / 1024 / 1024
#    print(f"[{tag}] {mem:.0f} MB")
#log_mem("start")

st.set_page_config(
    page_title="Dashboard",  # the page title shown in the browser tab
    page_icon=":telescope:",  # the page favicon shown in the browser tab
    layout="wide",  # page layout : use the entire screen
)
# add page title

st.title("Image Processing Dashboard")

#uploaded = st.file_uploader("Upload image", type=["jpg", "png"])

# --- #

process_btn = st.button("Process Image")
warning_placeholder = st.empty()

col1, col2 = st.columns([3,1])
with col1:
    image_placeholder = st.empty()
with col2:
    #nonsense_placeholder = st.empty()
    closeup_placeholder = st.empty()
    closeup_original_placeholder = st.empty()

total_cost1 = 0
total_cost2 = 0 
total_cost3 = 0
total_cost4 = 0 

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    #money1 = st.number_input("錢 - 主鏡", value=1000)
    total_placeholder1 = st.empty()
with col2:
    #money2 = st.number_input("錢 - 相機", value=1000)
    total_placeholder2 = st.empty()
with col3:
    #money3 = st.number_input("錢 - 赤道儀", value=1000)
    total_placeholder3 = st.empty()
with col4:
    #money4 = st.number_input("錢 - 觀測者", value=1000)
    total_placeholder4 = st.empty()
st.sidebar.write("") #為了讓遊戲玩壞的時候sidebar不會不見

st.header("類別")


with st.expander("所有類別"):
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        #with st.expander("主鏡"):
        st.header("主鏡")

        sth_placeholder = st.empty()
        category11_price = {
            "折射式望遠鏡": 0,
            "反射式望遠鏡": 0,
            "折反射式望遠鏡": 500,
        }
        category11 = st.selectbox("望遠鏡類型",list(category11_price.keys()))
        total_cost1 += category11_price[category11]
        sth_placeholder.write(f"首輪採買門檻：${total_cost1}")

    with col2:
        #with st.expander("相機"):
        st.header("相機")
        sth_placeholder = st.empty()
        category21_price = {
            "Canon": 100,
            "Nikon": 100,
            "Sony": 100,
            "天文相機": 1800
        }
        category21 = st.selectbox("相機類型/品牌",list(category21_price.keys()))
        total_cost2 += category21_price[category21]

        if category21 == "天文相機":
            category22_price = {
                "1/2'' ": 200,
                "4/3'' ": 800,
                "APS-C": 1600,
                "Full Frame": 2800
            }
            category22 = st.selectbox("感光元件規格",list(category22_price.keys()))
            total_cost2 += category22_price[category22]

        else:
            category22_price = {
                "APS-C": 400,
                "Full Frame": 800
            }
            category22 = st.selectbox("感光元件規格",list(category22_price.keys()))
            total_cost2 += category22_price[category22]
            if category22 =="APS-C":
                st.write("解析度上限24MP， \n視野大小縮小")
        sth_placeholder.write(f"首輪採買門檻：${total_cost2}")

    with col3:
        #with st.expander("觀測者"):
        st.header("拍攝天體")
        category31_options = {
            "M51 漩渦星系": {"index":1,"dimension_x":11,"dimension_y":7,"target_mag":21.3,"img_name":"m51-hubble-cr.tif", "file_id":"13R2ACNNVdyVIyPvz6Y_aR-JaV-moDBkN"}, #https://science.nasa.gov/asset/hubble/out-of-this-whirl-the-whirlpool-galaxy-m51-and-companion-galaxy/
            # 11477 x 7965
            "M81 波德星系": {"index":2,"dimension_x":27,"dimension_y":14,"target_mag":21.6,"img_name":"m81-hubble-cr.tif", "file_id":"1CzrbNVz_4K30yd2BweMdDxnnNuL_WcPQ"}, #https://science.nasa.gov/asset/hubble/hubble-photographs-grand-design-spiral-galaxy-m81/
            # 22620 x 15200
            "M8 礁湖星雲": {"index":3,"dimension_x":90,"dimension_y":54,"target_mag":22.0,"img_name":"m8-verarubin-cr.tif", "file_id":"1yw7kIl1pJxWA2fIpCnlylZrZnTDz1x9X"}, #https://rubinobservatory.org/gallery/collections/first-look-gallery/n4kvj0cemd5pbdqgtjdgp2jg2t
            # 10000 x 6131
            "M57 環狀星雲": {"index":4,"dimension_x":8,"dimension_y":8,"target_mag":20.8,"img_name":"m57-hubble.tif", "file_id":"10bjvBX-kffVZewulfx5yxihvnAERmTA_"}, #https://science.nasa.gov/asset/hubble/the-ring-nebula-m57/
            # 3179 x 3179
            "C42 星團": {"index":5,"dimension_x":20,"dimension_y":20,"target_mag":21.2,"img_name":"c42-hubble.tif", "file_id":"1NbqETsmOUgD-Z_jCNYYER06H1YIpsY5L"}, #https://esahubble.org/images/potw1137a/
            # 3851 x 3851
        }

        category31 = st.selectbox("拍攝天體",category31_options.keys())
        photo_index = category31_options[category31]["index"]
        dimension_x = category31_options[category31]["dimension_x"]
        dimension_y = category31_options[category31]["dimension_y"]
        img_file_name = category31_options[category31]["img_name"]
        target_mag = category31_options[category31]["target_mag"]
        file_id = category31_options[category31]["file_id"]

        st.metric("深空天體大小", f"{dimension_x:.0f}' x {dimension_y:.0f}'")

    with col4:
        st.header("觀測組...？")
        category41_choices = ["觀測組", "活動組"]
        category41 = st.selectbox("組別", category41_choices)
        if category41 == "活動組":
            st.write("你把遊戲玩壞了")
            st.stop()



st.header("可調變數")
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  

with col1:
    with st.expander("主鏡"):
        #st.header("主鏡")
        
        if category11 == "折射式望遠鏡":
            var12_price = {
                #300: 500,
                500: 1000,
                800: 1200,
                1200: 1400
            }
            var12 = st.selectbox("焦距 (mm)", list(var12_price.keys()))
            total_cost1 += var12_price[var12]
            if var12 == 300:
                var11_price = {
                    40: 0,
                    60: 450
                }
                var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
                total_cost1 += var11_price[var11]
            elif var12 == 500:
                var11_price = {
                    40: 0,
                    60: 450,
                    80: 1000,
                    100: 1600
                }
                var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
                total_cost1 += var11_price[var11]
            else:
                var11_price = {
                    40: 0,
                    60: 450,
                    80: 1000,
                    100: 1600,
                    120: 2400
                }
                var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
                total_cost1 += var11_price[var11]

            var13_price = {
                "除霧線": 200
            }
            var13 = st.multiselect("其他配備", var13_price.keys())
            total_cost1 += sum(var13_price[item] for item in var13) 
        
        elif category11 == "反射式望遠鏡":
            var12_price = {
                750: 800,
                1000: 1000,
                1600: 1250
            }
            var12 = st.selectbox("焦距 (mm)", list(var12_price.keys()))
            total_cost1 += var12_price[var12]

            var11_price = {
                30: 0,
                90: 1000,
                120: 2000,
                160: 3000
            }
            var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
            total_cost1 += var11_price[var11]

            var13_price = {
                "除霧線": 250
            }
            var13 = st.multiselect("其他配備", var13_price.keys())
            total_cost1 += sum(var13_price[item] for item in var13) 

        elif category11 == "折反射式望遠鏡":
            
            var12_price = {
                750: 750,
                1000: 1000,
                1500: 1250,
                2000: 1500,
                2500: 1750
            }
            var12 = st.selectbox("焦距 (mm)", list(var12_price.keys()))
            total_cost1 += var12_price[var12]

            if var12 == 750:
                var11_price = {
                    60: 0,
                    100: 750
                }
                var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
                total_cost1 += var11_price[var11]
            elif var12 == 1000:
                var11_price = {
                    60: 0,
                    100: 750,
                    140: 1500,
                }
                var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
                total_cost1 += var11_price[var11]
            elif var12 == 1500:
                var11_price = {
                    60: 0,
                    100: 750,
                    140: 1500,
                    195: 2400,
                }
                var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
                total_cost1 += var11_price[var11]
            else:
                var11_price = {
                    60: 0,
                    100: 750,
                    140: 1500,
                    195: 2400,
                    250: 3500
                }
                var11 = st.selectbox("口徑 (mm)", list(var11_price.keys()))
                total_cost1 += var11_price[var11]


            var13_price = {
                "除霧線": 250,
                "減焦環": 200
            }
            var13 = st.multiselect("其他配備", var13_price.keys())
            total_cost1 += sum(var13_price[item] for item in var13) 
            if "減焦環" in var13:
                var12 /= 2
        
with col2:
    with st.expander("相機"):
        #st.header("相機")
        if category21 == "天文相機":
            total_cost2 += 500
            if category22 == "1/2'' ":
                var21_price = {
                    "6 MP": 0,
                    "9 MP": 500
                }
                var21 = st.selectbox("解析度",list(var21_price.keys()))
                total_cost2 += var21_price[var21]
            elif category22 == "4/3'' ":       
                var21_price = {
                    "6 MP": 0,
                    "9 MP": 500,
                    "18 MP": 800
                }
                var21 = st.selectbox("像素",list(var21_price.keys()))
                total_cost2 += var21_price[var21]
            elif category22 == "APS-C": 
                var21_price = {
                    "18 MP": 200,
                    "24 MP": 900
                }
                var21 = st.selectbox("像素數量",list(var21_price.keys()))
                total_cost2 += var21_price[var21]
            elif category22 == "Full Frame": 
                var21_price = {
                    "24 MP": 0,
                    "40 MP": 1000,
                    "60 MP": 2000
                }
                var21 = st.selectbox("像素數量",list(var21_price.keys()))
                total_cost2 += var21_price[var21]

            var23_options = {
                "無":{"snr_boost":0.8,"price":0},
                "光害濾鏡": {"snr_boost":1,"price":600},
                "雙峰濾鏡": {"snr_boost":1.2,"price":1000}
            }
            var23 = st.selectbox("濾鏡", var23_options.keys())
            total_cost2 += var23_options[var23]["price"]
            snr_boost = var23_options[var23]["snr_boost"]

            st.write(f"訊噪比變為{1+snr_boost}倍")

            read_noise = 20
            if var21 == "6 MP": imgsize = (3000, 2000)
            elif var21 == "9 MP": imgsize = (3600, 2400)
            elif var21 == "18 MP": imgsize = (5100, 3400)
            elif var21 == "24 MP": imgsize = (6000, 4000)
            elif var21 == "40 MP": imgsize = (7800, 5200)
            elif var21 == "60 MP": imgsize = (8700, 5800)
        else:
            if category22 == "APS-C":
                #st.metric("像素數量上限26.2MP \n 視野大小縮小")
                var21_price = {
                    "9 MP": 0, # 3600 x 2400
                    "18 MP": 800, # 5100 x 3400
                    "24 MP": 1200
                }
                var21 = st.selectbox("像素數量",list(var21_price.keys()))
                total_cost2 += var21_price[var21]
            elif category22 == "Full Frame":
                if category21 == "Nikon":
                    var21_price = {
                        "24 MP": 1600, # 6000 x 4000
                        "34 MP": 2200, # 7200 x 4800
                        "46 MP": 2950 # 8250 x 5500
                    }
                    var21 = st.selectbox("像素數量",list(var21_price.keys()))
                    total_cost2 += var21_price[var21]
                else: 
                    var21_price = {
                        "18 MP": 900,
                        "24 MP": 1600,
                        "34 MP": 2200
                    }
                    var21 = st.selectbox("像素數量",list(var21_price.keys()))
                    total_cost2 += var21_price[var21]
            if var21 == "9 MP": imgsize = (3600, 2400)
            elif var21 == "18 MP": imgsize = (5100, 3400)
            elif var21 == "24 MP": imgsize = (6000, 4000)
            elif var21 == "34 MP": imgsize = (7200, 4800)
            elif var21 == "46 MP": imgsize = (8250, 5500)

            var22_options = {
                "高": {"read_noise":300, "price":200},
                "中": {"read_noise":100, "price":400},
                "低": {"read_noise":50, "price":600},
                "很低": {"read_noise":20, "price":800},
                "極低": {"read_noise":10, "price":1000}
            }
            var22 = st.selectbox("讀出雜訊", var22_options.keys())
            read_noise = var22_options[var22]["read_noise"]
            total_cost2 += var22_options[var22]["price"]

            var23_options = {
                "預設": {"snr_boost":0,"price":0},
                "改機（拆預設濾鏡）": {"snr_boost":0.1,"price":400},
                "光害濾鏡": {"snr_boost":0.2,"price":600},
                "雙峰濾鏡": {"snr_boost":0.4,"price":800}
            }
            var23 = st.selectbox("濾鏡", var23_options.keys())
            total_cost2 += var23_options[var23]["price"]
            snr_boost = var23_options[var23]["snr_boost"]
            st.write(f"訊噪比變為{1+snr_boost}倍（相較於一般相機預設濾鏡時）")
        

with col3:
    with st.expander("赤道儀、電瓶和愛心"):
        #st.header("赤道儀、電瓶和愛心")
        var31_price = {
            #"可載小型折射式": 400,
            "可載折射式望遠鏡": 900,
            "可載折反射式望遠鏡": 1300,
            "可載反射式望遠鏡": 1800
        }
        if category11 == "反射式望遠鏡":
            disable = {"可載小型折射式", "可載折射式望遠鏡", "可載折反射式望遠鏡"}
        elif category11 == "折反射式望遠鏡":
            disable = {"可載小型折射式", "可載折射式望遠鏡"}
        else:
            disable = {}

        var31 = st.selectbox("載重量",list(var31_price.keys()))
        total_cost3 += var31_price[var31]

        if var31 in disable:
            #if var31 == "可載小型折射式":
            #    st.write("口徑上限：60mm")
            st.warning(f"望遠鏡太重了，請升級")
            #st.stop()

        var32_options = {
            "60%": {"success_prob":0.6,"price":0},
            "80%": {"success_prob":0.8,"price":200},
            "90%": {"success_prob":0.9,"price":400},
            "95%": {"success_prob":0.95,"price":600},
            "98%": {"success_prob":0.98,"price":800},
            "99%": {"success_prob":0.99,"price":1000},
            "100%": {"success_prob":1,"price":1200},
        }
        var32 = st.selectbox("曝光成功率",var32_options.keys())
        total_cost3 += var32_options[var32]["price"]
        success_prob = var32_options[var32]["success_prob"]
        st.write("若失敗則曝光時間x0.1")
        #st.write("失敗率 = 100% - 成功率")

        var33_options = {
            "30s": {"single_shot_time":30, "price":0},
            "1 min": {"single_shot_time":60, "price":400},
            "2 min": {"single_shot_time":120, "price":600},
            "3 min": {"single_shot_time":180, "price":800},
            "5 min": {"single_shot_time":300, "price":1200}
        }
        var33 = st.selectbox("精準度：每張曝光時間",var33_options.keys())
        total_cost3 += var33_options[var33]["price"]
        single_shot_time = var33_options[var33]["single_shot_time"]

        var34_options = {
            "無": {"duration_limit":4,"price": 0},
            "弱": {"duration_limit":6,"price": 100},
            "中": {"duration_limit":8,"price": 300},
            "強": {"duration_limit":10,"price": 500},
            "大愛心": {"duration_limit":4,"price": 700}
        }
        var34 = st.selectbox("愛心氣氛",var34_options.keys())
        duration_limit1 = var34_options[var34]["duration_limit"]
        total_cost3 += var34_options[var34]["price"]
        if var34 == "無":
            st.write("曝光時間上限 = 4 hr")
        elif var34 == "弱":
            st.write("曝光時間上限 = 6 hr")
        elif var34 == "中":
            st.write("曝光時間上限 = 8 hr")
        elif var34 == "強":
            st.write("曝光時間無上限")                
        elif var34 == "大愛心":
            st.write("曝光時間上限 = 4 hr")

with col4:
    with st.expander("觀測者和天氣"):
        #st.header("觀測者和天氣")
        var41_options = {
            "0 hr":  {"duration": 0, "price": 0},
            "1 hr":  {"duration": 1, "price": 200},
            "2 hr":  {"duration": 2, "price": 400},
            "4 hr":  {"duration": 4, "price": 600},
            "6 hr":  {"duration": 6, "price": 800},
            "8 hr":  {"duration": 8, "price": 1000},
            "9 hr":  {"duration": 9, "price": 1200},
        }

        var41 = st.selectbox(
            "召喚好天氣的能力",
            var41_options.keys()
        )

        basic_duration = var41_options[var41]["duration"]
        total_cost4 += var41_options[var41]["price"]
        st.write("總曝光時間上限 = "+var41)

        var42_options = {
            "不健康": {"duration_limit":3,"price": 0},
            "還不錯": {"duration_limit":6,"price":200},
            "很好": {"duration_limit":10,"price":400}
        }
        var42 = st.selectbox("身體健康（清醒時數）",var42_options.keys())
        duration_limit2 = var42_options[var42]["duration_limit"]
        total_cost4 += var42_options[var42]["price"]

        if var42 =="不健康":
            st.write("曝光時間上限 = 3 hr")        
        elif var42 =="還不錯":
            st.write("曝光時間上限 = 6 hr")  
        elif var42 =="很好":
            st.write("曝光時間無上限")  

        var44_options = {
            "很糟": {"duration_loss":5,"price": 0},
            "初學": {"duration_loss":3,"price": 200},
            "中級": {"duration_loss":1,"price": 500},
            "高級": {"duration_loss":0,"price": 800}
        }
        var44 = st.selectbox("觀測技術",list(var44_options.keys()))
        duration_loss = var44_options[var44]["duration_loss"]
        total_cost4 += var44_options[var44]["price"]

        if var44 == "很糟":
            st.write("曝光時間 - 5hr")
        elif var44 == "初學":
            st.write("曝光時間 - 3hr")
        elif var44 == "中級":
            st.write("曝光時間 - 1hr")
        elif var44 == "高級":
            st.write("曝光時間不受影響")

        var43_options = {
            "臺大總圖前": {"basic-seeing":4.5,"as_prob": 0, "resolution_loss": 0, "price": 0, "sky_sqm": 18, "extinction":0.4},
            "雲海國小（但有雲）": {"basic-seeing":10,"as_prob": 0, "resolution_loss": 0, "price": 100,"sky_sqm": 20,"extinction":0.2},
            "新埔國小": {"basic-seeing":3,"as_prob": 0, "resolution_loss": 0, "price": 400,"sky_sqm": 20.5,"extinction":0.4},
            "五峰國小": {"basic-seeing":2.8,"as_prob": 0, "resolution_loss": 0, "price": 600,"sky_sqm": 21,"extinction":0.45},
            "觀星園": {"basic-seeing":2.5,"as_prob": 0, "resolution_loss": 0.1, "price": 1200,"sky_sqm": 21, "extinction":0.55},
            "梅峰": {"basic-seeing":2.4,"as_prob": 0, "resolution_loss": 0.1, "price": 1000,"sky_sqm": 21.5, "extinction":0.55},
            "昆陽": {"basic-seeing":2.1,"as_prob": 0.2, "resolution_loss": 0.2, "price": 1500,"sky_sqm": 21.7, "extinction":0.65},
            "塔塔加": {"basic-seeing":2.0,"as_prob": 0.2, "resolution_loss": 0.3, "price": 1600,"sky_sqm": 21.7, "extinction":0.6},
            "小風口": {"basic-seeing":1.8,"as_prob": 0.4,"resolution_loss": 0.4, "price": 2000,"sky_sqm": 22.0, "extinction":0.7}
        }
        var43 = st.selectbox("觀測地點",var43_options.keys())
        total_cost4 += var43_options[var43]["price"]
        as_prob_basic = var43_options[var43]["as_prob"]
        sky_sqm = var43_options[var43]["sky_sqm"]
        resolution_loss = var43_options[var43]["resolution_loss"]
        basic_seeing = var43_options[var43]["basic-seeing"]
        extinction = var43_options[var43]["extinction"]

        if var43 == "觀星園" or var43 =="梅峰":
            st.write("若無除霧線解析度降低10%")
        elif var43 == "昆陽":
            st.write("若無除霧線解析度降低20%")
            st.write("高山症機率+20%")
        elif var43 == "塔塔加":
            st.write("若無除霧線解析度降低30%")
            st.write("高山症機率+20%")
        elif var43 == "小風口":
            st.write("若無除霧線解析度降低40%")
            st.write("高山症機率+40%")

        var45_options = {
            "0%": {"as_resist":0,"price":0},
            "50%": {"as_resist":0.5,"price":200},
            "75%": {"as_resist":0.75,"price":300},
            "95%": {"as_resist":0.95,"price":400},
            "100%": {"as_resist":1,"price":500}
        }
        var45 = st.selectbox("抗高山症機率",var45_options.keys())
        total_cost4 += var45_options[var45]["price"]
        as_resist = var45_options[var45]["as_resist"]   
        st.write("高山症發作機率= 原高山症機率x(1-抗高山症機率)")
        st.write("若高山症發作則曝光時數x0.3")


# sidebar - metavariables #
#st.sidebar.title("Controls")

# pixel-size (um)
if category22 == "1/2'' ":
    sensor_x = 6.6
    sensor_y = 4.4
elif category22 == "4/3'' ":
    sensor_x = 17.3
    sensor_y = 13
elif category22 == "APS-C":
    sensor_x = 23.6
    sensor_y = 15.7
elif category22 == "Full Frame":
    sensor_x = 36
    sensor_y = 24    

total_pixel = float(var21.replace("MP", ""))*1e6
pixel_size = np.sqrt(sensor_x*sensor_y*1e6/total_pixel)
pixel_angle = 206*pixel_size/var12


frame_x = 206265/60*sensor_x/var12
frame_y = 206265/60*sensor_y/var12
# fov = diagonal length of full frame
fov = 206265/60*43.26/var12



duration_hr_theo = max([min([basic_duration, duration_limit1, duration_limit2]) - duration_loss,0])
as_prob = as_prob_basic * (1-as_resist)
success_prob = success_prob

#******#
actual_duration_hr = duration_hr_theo
expected_duration_hr = (as_prob*0.3+(1-as_prob)) * (success_prob+(1-success_prob)*0.1)*duration_hr_theo 

target_mag = target_mag
target_electron_flux = 10.9*pixel_size*pixel_size*np.power(0.398,target_mag-20)*extinction
sky_electron_flux = 10.9*pixel_size*pixel_size*np.power(0.398,sky_sqm-20)

quantum_eff = 0.5

snr = np.sqrt(actual_duration_hr*3600)*target_electron_flux*quantum_eff/np.sqrt((target_electron_flux+sky_electron_flux)*quantum_eff+read_noise*10/single_shot_time)*(1+snr_boost)/40

if "除霧線" not in var13:
    seeing_multiplier = 1 + resolution_loss
else: 
    seeing_multiplier = 1
seeing = var12/206*basic_seeing/pixel_size*seeing_multiplier
resolution_ph = 1.2*1000*6.563e-4/var11*var12/pixel_size 
resolution = np.sqrt(seeing*seeing+resolution_ph*resolution_ph)

#st.sidebar.metric("視野大小", f"{fov:.1f}'")
st.sidebar.metric("畫面大小", f"{frame_x:.0f}' x {frame_y:.0f}'")
#st.sidebar.metric("像素大小 (μm)", f"{pixel_size:.2f}")
#st.sidebar.metric("像素角度 ", f"{pixel_angle:.1f}''")
st.sidebar.metric("訊噪比", f"{snr:.0f}")
st.sidebar.metric("解析度（像素）", f"{resolution:.2f}")
st.sidebar.metric("大氣解析度（像素）", f"{seeing:.2f}")
st.sidebar.metric("物理解析度（像素）", f"{resolution_ph:.2f}")

st.sidebar.metric("曝光時間上限 (hr)", f"{duration_hr_theo}")
st.sidebar.metric("曝光時間期望值 (hr)", f"{expected_duration_hr:.1f}")
#st.sidebar.metric("曝光成功率", f"{success_prob}")
#st.sidebar.metric("高山症機率", f"{as_prob}")



total_placeholder1.metric("Total cost", f"${total_cost1}")
total_placeholder2.metric("Total cost", f"${total_cost2}")
total_placeholder3.metric("Total cost", f"${total_cost3}")
total_placeholder4.metric("Total cost", f"${total_cost4}")

#log_mem("before processing")

import gc
from skimage.filters import gaussian
import numpy as np

#@st.cache_data
#def load_image(path):
#    img = Image.open(path)
#    return img
#img = load_image(f"img/{img_file_name}")

import requests
from io import BytesIO
url = f"https://drive.google.com/uc?export=download&id={file_id}"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

def resize_and_crop(img, frame_x, frame_y, imgsize):
    w, h = img.size
    if dimension_y > dimension_x * h/w:
        source_angle_per_pixel = dimension_x / w
        scale_percentage_x = frame_x / dimension_x
        scale_percentage_y = frame_y / dimension_x *w/h
    else:
        scale_percentage_x = frame_x / dimension_y *h/w
        scale_percentage_y = frame_y / dimension_y

    y0 = (h - scale_percentage_y * h)//2
    y1 = y0+scale_percentage_y * h
    x0 = (w - scale_percentage_x * w)//2
    x1 = x0+scale_percentage_x * w
    cropped = img.crop((x0, y0, x1, y1))
    resized = cropped.resize(imgsize)
    return resized

# Optimized: Modifies input in-place where possible to save memory
def add_noise_and_blur_optimized(pil_img, snr, resolution_radius):
    
    # 1. Convert to Float32 ONCE (Primary Allocation)
    # normalizing to 0-1 immediately
    img_arr = np.array(pil_img, dtype=np.float32)
    img_arr /= 255.0
    
    # --- Step 1: Noise (In-Place Optimization) ---
    signal_power = np.mean(img_arr ** 2)
    noise_power = signal_power / snr
    
    # Generate noise directly into a temporary buffer
    noise = np.random.normal(
        loc=0.0, 
        scale=np.sqrt(noise_power), 
        size=img_arr.shape
    ).astype(np.float32)
    
    # Add noise to image IN-PLACE (avoids creating a 3rd full image copy)
    img_arr += noise
    
    # Delete noise buffer immediately
    del noise 
    
    # Clip IN-PLACE
    np.clip(img_arr, 0.0, 1.0, out=img_arr)
    
    # --- Step 2: Gaussian Blur ---
    # Determine channel axis
    channel_axis = -1 if img_arr.ndim == 3 else None
    
    # Run filter (Produces new array, can't be helped easily with skimage)
    blurred = gaussian(
        img_arr,
        sigma=resolution_radius,
        channel_axis=channel_axis,
        preserve_range=True
    ).astype(np.float32) # Ensure we stay float32
    
    # Delete the pre-blur image immediately to free memory
    del img_arr
    gc.collect() # Force memory release
    
    # --- Step 3: Finalize ---
    # Clip IN-PLACE
    np.clip(blurred, 0.0, 1.0, out=blurred)
    
    # Convert to uint8 (0-255)
    blurred *= 255
    final_uint8 = blurred.astype(np.uint8)
    
    # Clean up last float buffer
    del blurred
    gc.collect()
    
    return final_uint8

def process_image_from_img1(_img1, resolution_radius):
    #log_mem("Start processing")
    # Using the optimized combined function to manage memory tight
    result = add_noise_and_blur_optimized(_img1, snr, resolution_radius)
    #log_mem("End processing")
    return result

#@st.cache_data
def closeup(img, width):
    w, h = img.size
    y0 = (h-width)//2
    y1 = (h+width)//2
    x0 = (w-width)//2
    x1 = (w+width)//2
    cropped = img.crop((x0, y0, x1, y1))
    return cropped

#@st.cache_data
def closeup_original(_img_original, img_resized, width):
    w1, h1 = img_resized.size
    scale_percentage_x1 = width/w1
    scale_percentage_y1 = width/h1
    w, h = _img_original.size

    if dimension_y > dimension_x * h/w:
        scale_percentage_x2 = frame_x / dimension_x
        scale_percentage_y2 = frame_y / dimension_x *w/h
    else:
        scale_percentage_x2 = frame_x / dimension_y *h/w
        scale_percentage_y2 = frame_y / dimension_y

    scale_percentage_x = scale_percentage_x1 * scale_percentage_x2
    scale_percentage_y = scale_percentage_y1 * scale_percentage_y2
    
    y0 = (h - scale_percentage_y * h)//2
    y1 = y0+scale_percentage_y * h
    x0 = (w - scale_percentage_x * w)//2
    x1 = x0+scale_percentage_x * w
    cropped = _img_original.crop((x0, y0, x1, y1))
    return cropped

# --- Main Execution ---


if process_btn:
    if snr < 1:
        warning_placeholder.warning("訊噪比小於1")
        image_placeholder.empty()
        closeup_placeholder.empty()
        closeup_original_placeholder.empty()

    else:
        if var31 in disable:
            warning_placeholder.warning("望遠鏡太重了，請升級")
        else:
            with st.spinner("Processing image..."):
                
                resolution_radius = resolution / 2
                
                # 1. Main Process
                img1 = resize_and_crop(img, frame_x, frame_y, imgsize)
                final_img = process_image_from_img1(img1, resolution_radius)
                image_placeholder.image(final_img, caption="Processed Image")
                
                # 2. Closeup Process
                width = 600
                closeup0 = closeup(img1, width)
                closeup_img = process_image_from_img1(closeup0, resolution_radius)
                closeup_placeholder.image(
                    closeup_img,
                    caption="Processed image cropped, 5cm x 5cm"
                )
    
                # 3. Original Closeup Process
                closeup_ori = closeup_original(img, img1, width)
                closeup_original_placeholder.image(
                    closeup_ori,
                    caption="Original image cropped, 5cm x 5cm"
                )
