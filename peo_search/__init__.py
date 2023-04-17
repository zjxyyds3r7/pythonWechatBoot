import pandas as pd


def get_sex(id: str):
    if len(id) == 19:
        id = id[0:18]
    if len(id) != 18:
        return None
    if int(id[-2]) % 2 == 0:
        return '女'
    else:
        return '男'


def get_bir_year(id: str):
    if len(id) == 19:
        id = id[0:18]

    if len(id) != 18:
        return -1
    return int(id[6:10])


def get_bir_month(id: str):
    if len(id) == 19:
        id = id[0:18]

    if len(id) != 18:
        return -1
    return int(id[10:12])


def get_bir_day(id: str):
    if len(id) == 19:
        id = id[0:18]

    if len(id) != 18:
        return -1
    return int(id[12:14])


def get_garde(classid: str):
    return int(classid[0])


def get_class(classid: str):
    return int(classid[2:4])


def get_stu_info(path: str):
    all_stu = pd.read_excel('t.xlsx')
    no_non_stu = all_stu.dropna(axis=0, how='any')
    stu_data_res = pd.DataFrame()
    stu_data_res['school'] = "实验高中"
    stu_data_res['garde'] = no_non_stu.apply(lambda x: get_garde(x['班级']), axis=1)
    stu_data_res['class'] = no_non_stu.apply(lambda x: get_class(x['班级']), axis=1)
    stu_data_res['name'] = no_non_stu['姓名']
    try:
        stu_data_res['sex'] = no_non_stu.apply(lambda x: get_sex(str(int(x['身份证号']))), axis=1)
        stu_data_res['bir_year'] = no_non_stu.apply(lambda x: get_bir_year(str(int(x['身份证号']))), axis=1).astype('int64')
        stu_data_res['bir_month'] = no_non_stu.apply(lambda x: get_bir_month(str(int(x['身份证号']))), axis=1)
        stu_data_res['bir_day'] = no_non_stu.apply(lambda x: get_bir_day(str(int(x['身份证号']))), axis=1)
    except:
        stu_data_res['sex'] = no_non_stu.apply(lambda x: get_sex(str((x['身份证号']))), axis=1)
        stu_data_res['bir_year'] = no_non_stu.apply(lambda x: get_bir_year(str((x['身份证号']))), axis=1).astype('int64')
        stu_data_res['bir_month'] = no_non_stu.apply(lambda x: get_bir_month(str((x['身份证号']))), axis=1)
        stu_data_res['bir_day'] = no_non_stu.apply(lambda x: get_bir_day(str((x['身份证号']))), axis=1)
    stu_data_res['school'] = "实验高中"
    stu_data_res = stu_data_res.dropna(axis=0, how='any')

    # print(stu_data_res)
    # print(stu_data[stu_data['name'].str.contains('王俊翰')])

    all_stu = pd.read_excel('t1.xlsx')
    no_non_stu = all_stu.dropna(axis=0, how='all')
    stu_data = pd.DataFrame()
    stu_data['school'] = "美高"
    stu_data['class'] = no_non_stu['班级']
    stu_data['name'] = no_non_stu['姓名']
    try:
        stu_data['sex'] = no_non_stu.apply(lambda x: get_sex(str(int(x['身份证号']))), axis=1)
        stu_data['bir_year'] = no_non_stu.apply(lambda x: get_bir_year(str(int(x['身份证号']))), axis=1).astype('int64')
        stu_data['bir_month'] = no_non_stu.apply(lambda x: get_bir_month(str(int(x['身份证号']))), axis=1)
        stu_data['bir_day'] = no_non_stu.apply(lambda x: get_bir_day(str(int(x['身份证号']))), axis=1)
    except:
        stu_data['sex'] = no_non_stu.apply(lambda x: get_sex(str((x['身份证号']))), axis=1)
        stu_data['bir_year'] = no_non_stu.apply(lambda x: get_bir_year(str((x['身份证号']))), axis=1).astype('int64')
        stu_data['bir_month'] = no_non_stu.apply(lambda x: get_bir_month(str((x['身份证号']))), axis=1)
        stu_data['bir_day'] = no_non_stu.apply(lambda x: get_bir_day(str((x['身份证号']))), axis=1)
    stu_data['school'] = "美高"
    stu_data['garde'] = 3
    # print(stu_data)
    df3 = pd.concat([stu_data_res, stu_data])
    # print(df3)
    return df3


i = get_stu_info("")


def search(stuinfo=i, name=""):
    res = stuinfo.copy()
    if name != '':
        res = res[res['name'].str.contains(name)]
    return res.values.tolist()


if __name__ == "__main__":
    r = search(name='周')
    # print(r, len(r))
    res = ""
    for i in r:
        res += "{0} {1}年{2:2}班 {3:4} 性别:{4} 出生于:{5}年{6:2}月{7:2}日\n".format(*i)
    print(res)

