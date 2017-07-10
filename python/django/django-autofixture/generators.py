from autofixture.generators import Generator
import random
import string


def random_string(length, type_random=None):
    if type_random == "NUMBER":
        choice = string.digits
    elif type_random == "WORD":
        choice = string.ascii_lowercase
    else:
        choice = string.digits + string.ascii_lowercase
    return ''.join(random.choice(choice) for i in range(length))


class PhoneGenerator(Generator):
    """ Generates a phone """

    network = ['096', '098', '097']

    def __init__(self, *args, **kwargs):
        super(PhoneGenerator, self).__init__(*args, **kwargs)

    def generate(self):
        return random.choice(self.network) + random_string(7, "NUMBER")


class FileNameGenerator(Generator):
    """Generates a filename"""

    def __init__(self, ext='jpg', *args, **kwargs):
        self.ext = ext
        super(FileNameGenerator, self).__init__(*args, **kwargs)

    def generate(self):
        return "{}.{}".format(random_string(6, 'WORD'), self.ext)


class CompanyNameGenerator(Generator):
    """Generates a company name"""

    company_names = ["Shangqiu Kunda Trading Co., Ltd.",
                     "Dongguan Haohoo Clothing Co., Ltd.",
                     "Yiwu City Lisheng Trading Co., Ltd.",
                     "Ningbo Wealthy Industry & Trade Co., Ltd.",
                     "Sky Aim Industries",
                     "Sonay Tekstil Sanayi Ve Ticaret Limited Sirketi",
                     "Quanzhou St. Source Police Surveillance Equipment Co., Ltd.",
                     "Hangzhou Fuhan Garment Accessories Co., Ltd.",
                     "Suihua Jingfangmei Trading Co., Ltd.",
                     "Shanghai Jingzhi Apparel Co., Ltd.",
                     "Guangzhou Xy Printing Co., Ltd.",
                     "Thai Handicraft Co., Ltd.",
                     "Shaoxing Aifuer Embroidery Co., Ltd.",
                     "Shanghai Mengshen International Trade Co., Ltd.",
                     "Hebei Hanlin Textile Co., Ltd.",
                     "Dongguan Hongguo Leather Co., Ltd.",
                     "Shenze County Shengda Textile Co., Ltd.",
                     "Haining Sunks Textile Co., Ltd.",
                     "Minhong (Xuchang City) Imp. & Exp. Co., Ltd.",
                     "Shaanxi Tongyu Industry And Trade Co., Ltd.",
                     "Yangzhou Lianhe Nonwoven Material Factory",
                     "Qiaoxi Dist. Zhongmei Fur Firm (Shijiazhuang)",
                     "Bignine International Trade (Dalian) Co., Ltd.",
                     "Shijiazhuang Yingda Textile Co., Ltd.",
                     "Jinjiang King Lion Tarding Co., Ltd.",
                     "Al-Aspania Company For Producing And Trading Natural Fertilizer",
                     "Dongguan Jiali Leather Co., Ltd.",
                     "Shaoxing Firsten Electronics Co., Ltd.",
                     "Joy Foods (Zhangzhou) Co., Ltd.",
                     "Thai Unionbone Co.,Ltd",
                     "Melnitsa Varna 2006 Ood",
                     "Dalian Young Foods Co., Ltd.",
                     "Dalian Kerrybright Food Co., Ltd.",
                     "Cofco Hebei International Trading Co., Ltd.",
                     "Tropical Link Canada Ltd",
                     "Shanker International",
                     "Roman Export Limited",
                     "Sabnaz International Trading Corporation",
                     "Hebei Tomato Industry Co., Ltd.",
                     "Hangzhou Gujia Leisure Goods Co., Ltd.",
                     "R&W Inc",
                     "May Zest Tea Co., Ltd.",
                     "Trang Ly Pharma Trade Company Limited",
                     "K.Y.C",
                     "Chen En Food Product Enterprise Co., Ltd.",
                     "Velocitum Pty.Ltd",
                     "Brain Trust Co., Ltd.",
                     "Wedesignit! Yourepit! Limited",
                     "Xiamen Aicai Apparel Co., Ltd.",
                     "Pujiang Rongsheng Garment Factory"]

    def generate(self):
        return random.choice(self.company_names)
