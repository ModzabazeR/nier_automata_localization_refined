from rich.console import Console
from typing import List

# Elements in the list can be:
# 1. Range of code points in the destructed list format || e.g. `*list(range({start unicode (inclusive)}, {end unicode (exclusive)}))` ||
# 2. A single code point (eg. just 0x0e01)
chars_to_add: List[int] = [
    # Thai glyphs (https://www.compart.com/en/unicode/block/U+0E00)
    # Change it to your language unicode range (see: https://www.compart.com/en/unicode/block)
    # Note that some code point in the block might not be used. For example, in Thai block, the
    # range is 0x0e00 - 0x0e7f but 0x0e3b - 0x0e3e and 0x0e5c - 0x0e7f is not used.
    # only add the code point that is used in the font.
    *list(range(0x0e01, 0x0e31)),
    *list(range(0x0e3f, 0x0e47)),
    *list(range(0x0e4f, 0x0e5c)),
]

# can be changed to jp, en, fr, it, de, es
srcLang = "jp"
# your language
targetLang = "th"

langFormats = {
    "jp": {
        "default": "",
        "novel": ""
    },
    "en": {
        "default": "_us",
        "novel": "_eng"
    },
    "fr": {
        "default": "_fr",
        "novel": "_fra"
    },
    "it": {
        "default": "_it",
        "novel": "_ita"
    },
    "de": {
        "default": "_de",
        "novel": "_ger"
    },
    "es": {
        "default": "_es",
        "novel": "_esp"
    },
}

gameStrings = {
    "core/corehap.dat": {
        "bin": [
            "global_d595bcd1_scp", 
            "global_60efb803_scp", 
            "global_638e40c8_scp"
        ],
        "pak": ["core_hap"],
    },
    "ph1/p100.dat": {
        "bin": [
            "p100_fa238e7c_scp", 
            "p100_c6ab1d8f_scp", 
            "p100_dfcc155d_scp", 
            "p100_7f31f924_scp", 
            "p100_d8a4a747_scp", 
            "p100_e1dc4db4_scp", 
            "p100_e2d39d13_scp", 
            "p100_440fda42_scp", 
            "p100_536bd4fb_scp", 
            "p100_7c282dc8_scp", 
            "p100_cbfd7706_scp", 
            "p100_6a34d49e_scp", 
            "p100_301b50d3_scp", 
            "p100_5f2b7c58_scp", 
            "p100_a85f65ec_scp", 
            "p100_10a1b8c_scp", 
            "p100_8371cfcf_scp", 
            "p100_54edd5c_scp", 
            "p100_ce928ad9_scp", 
            "p100_89910ddf_scp", 
            "p100_a5817204_scp", 
            "p100_6695192d_scp", 
            "p100_4aa7dace_scp", 
            "p100_43f203b8_scp", 
            "p100_90998b13_scp", 
            "p100_973474b4_scp", 
            "p100_69ab2de6_scp", 
            "p100_643b9449_scp", 
            "p100_306867fd_scp", 
            "p100_61b598fd_scp", 
            "p100_39cda07a_scp", 
            "p100_9092a1f1_scp", 
            "p100_1a401b0f_scp", 
            "p100_ec82f9bf_scp", 
            "p100_cb2621f3_scp", 
            "p100_56f39801_scp", 
            "p100_6fc2accc_scp", 
            "p100_824dfa10_scp", 
            "p100_508c029e_scp", 
            "p100_a2a7da53_scp", 
            "p100_23622eee_scp", 
            "p100_56e518db_scp", 
            "p100_2299a056_scp", 
            "p100_73ce9cac_scp", 
            "p100_adc09aec_scp", 
            "p100_81c8f672_scp", 
            "p100_47a5d6eb_scp", 
            "p100_9b15340d_scp", 
            "p100_264b174c_scp"
        ]
    },
    "ph2/p200.dat": {
        "bin": [
            "p200_a2a7da53_scp", 
            "p200_2e8bdcb0_scp", 
            "p200_886c2178_scp", 
            "p200_92dddd6e_scp", 
            "p200_bb51fdfc_scp", 
            "p200_b99094bd_scp", 
            "p200_20084f1f_scp", 
            "p200_a3d6d2f5_scp", 
            "p200_7c0c6f18_scp", 
            "p200_c544d6ad_scp", 
            "p200_78334de1_scp", 
            "p200_24125524_scp", 
            "p200_7398bbfd_scp", 
            "p200_24194e13_scp", 
            "p200_647d1cd7_scp", 
            "p200_3c562f91_scp", 
            "p200_ff3d446f_scp", 
            "p200_d0b71b3b_scp", 
            "p200_71c59d9f_scp", 
            "p200_8cbb3f1e_scp", 
            "p200_2bfce9ed_scp", 
            "p200_48a7f0fd_scp", 
            "p200_6ae550e0_scp", 
            "p200_96e13a06_scp", 
            "p200_ad4026af_scp", 
            "p200_8182a35a_scp", 
            "p200_27db07bb_scp", 
            "p200_20cd934d_scp", 
            "p200_5dfcaace_scp", 
            "p200_e723b449_scp", 
            "p200_a1e11071_scp", 
            "p200_e8fce7cc_scp", 
            "p200_4b245f40_scp", 
            "p200_c7ba8911_scp", 
            "p200_f764463b_scp", 
            "p200_a68c4ea9_scp", 
            "p200_e8cf2a5c_scp", 
            "p200_58623dde_scp", 
            "p200_d5ac1e7d_scp", 
            "p200_1cc100aa_scp", 
            "p200_398cde2c_scp", 
            "p200_f1f22ca2_scp", 
            "p200_aad478cc_scp", 
            "p200_7914bf_scp", 
            "p200_c44b75b3_scp", 
            "p200_b4fc12d6_scp", 
            "p200_1fcb850d_scp", 
            "p200_67909aeb_scp", 
            "p200_8806bcb7_scp", 
            "p200_7793b6d6_scp", 
            "p200_17d05835_scp", 
            "p200_99454795_scp", 
            "p200_56645a4b_scp", 
            "p200_9a8a8724_scp", 
            "p200_8767f81e_scp", 
            "p200_40b3c93d_scp", 
            "p200_c3ab84c7_scp", 
            "p200_d0a7f4dc_scp", 
            "p200_cc694d55_scp", 
            "p200_7a5876f7_scp", 
            "p200_d75fa9d2_scp", 
            "p200_dad50fa7_scp", 
            "p200_9dd3606e_scp", 
            "p200_6aa3f28e_scp", 
            "p200_2311697b_scp", 
            "p200_1de99b24_scp", 
            "p200_3456f87_scp", 
            "p200_8118914c_scp", 
            "p200_5a63902e_scp", 
            "p200_2fb68036_scp"
        ]
    },
    "ph3/p300.dat": {
        "bin": [
            "p300_f80fe22d_scp", 
            "p300_abb1d768_scp", 
            "p300_69ab2de6_scp", 
            "p300_fe415e44_scp", 
            "p300_e9106cc6_scp", 
            "p300_a60ff1fc_scp", 
            "p300_d578eca9_scp", 
            "p300_26ad4903_scp", 
            "p300_8352dd61_scp", 
            "p300_1cc46857_scp", 
            "p300_a34d9d8a_scp", 
            "p300_2ac25a34_scp", 
            "p300_e47baab_scp", 
            "p300_73ee82d4_scp", 
            "p300_1c94bbb3_scp", 
            "p300_969b4cd4_scp", 
            "p300_52095a27_scp", 
            "p300_5f56e621_scp", 
            "p300_d7fb6a72_scp", 
            "p300_a80afa1d_scp", 
            "p300_58e3f469_scp", 
            "p300_b863f435_scp", 
            "p300_4ac43a7f_scp", 
            "p300_f29af5ee_scp", 
            "p300_59a32047_scp", 
            "p300_ebb2aa60_scp", 
            "p300_2b0332c8_scp", 
            "p300_8f18b72c_scp", 
            "p300_78ebd792_scp", 
            "p300_4fce2323_scp", 
            "p300_abb0feab_scp", 
            "p300_7677d46d_scp", 
            "p300_33eec348_scp", 
            "p300_312ca323_scp", 
            "p300_b01535dd_scp", 
            "p300_6f88066d_scp", 
            "p300_454d3c27_scp", 
            "p300_fb6b9581_scp", 
            "p300_838131a5_scp", 
            "p300_540e0da_scp", 
            "p300_e3d05ab7_scp", 
            "p300_dd8b37bd_scp", 
            "p300_9d8df164_scp", 
            "p300_af5fb37c_scp", 
            "p300_d48627b4_scp", 
            "p300_34ffac43_scp", 
            "p300_2460bab4_scp", 
            "p300_fe580523_scp", 
            "p300_be18477d_scp", 
            "p300_7220e53d_scp", 
            "p300_79a7d0d0_scp", 
            "p300_cc42e29e_scp", 
            "p300_d86d80b1_scp", 
            "p300_fb5ab100_scp", 
            "p300_62973173_scp", 
            "p300_249dcf6a_scp", 
            "p300_f0e6bd59_scp", 
            "p300_95a183ba_scp", 
            "p300_24fd47f4_scp", 
            "p300_50eb25b8_scp", 
            "p300_ac91bbe4_scp", 
            "p300_d913dcc1_scp", 
            "p300_df90c81a_scp", 
            "p300_54b1765c_scp", 
            "p300_9b77492c_scp", 
            "p300_4a0a3acc_scp", 
            "p300_157c0c19_scp", 
            "p300_802d17e9_scp", 
            "p300_fca61b8d_scp", 
            "p300_544f9315_scp", 
            "p300_987be645_scp", 
            "p300_68b9c234_scp", 
            "p300_10112854_scp", 
            "p300_d2ca712b_scp", 
            "p300_7de5c329_scp", 
            "p300_f4f38872_scp", 
            "p300_4716685f_scp", 
            "p300_e6cf440a_scp", 
            "p300_22633b31_scp", 
            "p300_ae2eada6_scp", 
            "p300_d2de713_scp", 
            "p300_c0c1e86c_scp", 
            "p300_e4c7a829_scp"
        ]
    },
    "ph4/p400.dat": {
        "bin": [
            "p400_b0e38442_scp", 
            "p400_fc21ced3_scp", 
            "p400_3af366c3_scp", 
            "p400_5b4661f4_scp", 
            "p400_42374ea5_scp", 
            "p400_1afc5db6_scp", 
            "p400_5489214b_scp"
        ]
    },
    "phf/pf10.dat": {
        "bin": ["pf10_7de5c329_scp"],
    },
    "phf/pf30.dat": {
        "bin": ["pf30_148bec7a_scp"],
    },
    "phf/pf31.dat": {
        "bin": ["pf31_d2ca712b_scp"],
    },
    "phf/pf60.dat": {
        "bin": ["pf60_149e7cbe_scp"],
    },
    "quest/q020.dat": {
        "bin": ["q020_404eba3d_scp"],
    },
    "quest/q031.dat": {
        "bin": ["q031_b551328a_scp"],
    },
    "quest/q032.dat": {
        "bin": ["q032_94bdfeb7_scp"],
    },
    "quest/q040.dat": {
        "bin": ["q040_cf7c14d9_scp"],
    },
    "quest/q070.dat": {
        "bin": ["q070_fb360535_scp"],
    },
    "quest/q071.dat": {
        "bin": ["q071_1a17171a_scp"],
    },
    "quest/q080.dat": {
        "bin": ["q080_64afc72a_scp"],
    },
    "quest/q090.dat": {
        "bin": [
            "q090_11b12a94_scp", 
            "q090_86062922_scp", 
            "q090_105d4edd_scp"
        ],
    },
    "quest/q091.dat": {
        "bin": [
            "q091_def6c866_scp",
            "q091_402dfd2e_scp",
            "q091_e03615dd_scp",
            "q091_2f2a0eea_scp",
        ],
    },
    "quest/q092.dat": {
        "bin": [
            "q092_3cd7f934_scp",
            "q092_35330df_scp",
            "q092_82c2e878_scp",
        ],
    },
    "quest/q095.dat": {
        "bin": ["q095_fc4d3b85_scp"]
    },
    "quest/q100.dat": {
        "bin": ["q100_f4f7e973_scp"]
    },
    "quest/q101.dat": {
        "bin": ["q101_5be5b4cc_scp"]
    },
    "quest/q102.dat": {
        "bin": ["q102_28e223f7_scp"]
    },
    "quest/q103.dat": {
        "bin": ["q103_d2b3f5a6_scp"]
    },
    "quest/q104.dat": {
        "bin": ["q104_e9ff21ee_scp"]
    },
    "quest/q110.dat": {
        "bin": ["q110_171236f0_scp"]
    },
    "quest/q120.dat": {
        "bin": ["q120_8dcd7a1a_scp"]
    },
    "quest/q121.dat": {
        "bin": ["q121_70545c1f_scp"]
    },
    "quest/q122.dat": {
        "bin": ["q122_3a5128c8_scp"]
    },
    "quest/q123.dat": {
        "bin": ["q123_6fde04e_scp"]
    },
    "quest/q130.dat": {
        "bin": ["q130_b68bfe22_scp"]
    },
    "quest/q140.dat": {
        "bin": ["q140_7cda31e_scp"]
    },
    "quest/q150.dat": {
        "bin": ["q150_d31e5833_scp"]
    },
    "quest/q160.dat": {
        "bin": ["q160_d8b9d0be_scp"]
    },
    "quest/q162.dat": {
        "bin": ["q162_fc7da4a2_scp"]
    },
    "quest/q170.dat": {
        "bin": ["q170_96333b78_scp"]
    },
    "quest/q171.dat": {
        "bin": ["q171_12f2963a_scp"]
    },
    "quest/q180.dat": {
        "bin": ["q180_2d2126d2_scp"]
    },
    "quest/q181.dat": {
        "bin": ["q181_746d944f_scp"]
    },
    "quest/q210.dat": {
        "bin": ["q210_a6306d6c_scp"]
    },
    "quest/q220.dat": {
        "bin": ["q220_e880784a_scp"]
    },
    "quest/q221.dat": {
        "bin": ["q221_b113244a_scp"]
    },
    "quest/q222.dat": {
        "bin": ["q222_f8217e42_scp"]
    },
    "quest/q290.dat": {
        "bin": ["q290_e15f2fa1_scp"]
    },
    "quest/q300.dat": {
        "bin": ["q300_5f9ed04e_scp"]
    },
    "quest/q330.dat": {
        "bin": [
            "q330_21f485e_scp",
            "q330_70a701da_scp",
            "q330_9bafd382_scp",
            "q330_b853020f_scp",
            "q330_ee317264_scp",
        ]
    },
    "quest/q340.dat": {
        "bin": ["q340_5620eb59_scp"]
    },
    "quest/q360.dat": {
        "bin": ["q360_8efed5ef_scp"]
    },
    "quest/q400.dat": {
        "bin": [
            "q400_1f6199eb_scp",
            "q400_21ca35cb_scp",
            "q400_48d76c20_scp",
            "q400_fc5b48ad_scp",
        ]
    },
    "quest/q401.dat": {
        "bin": ["q401_643e5418_scp"]
    },
    "quest/q403.dat": {
        "bin": ["q403_5d43ba8b_scp"]
    },
    "quest/q410.dat": {
        "bin": ["q410_4f2b901a_scp"]
    },
    "quest/q440.dat": {
        "bin": ["q440_3b4ef61d_scp"]
    },
    "quest/q500.dat": {
        "bin": ["q500_8446c06e_scp"]
    },
    "quest/q520.dat": {
        "bin": ["q520_afd5aa67_scp"]
    },
    "quest/q532.dat": {
        "bin": ["q532_65ff89bf_scp"]
    },
    "quest/q540.dat": {
        "bin": ["q540_e1207097_scp"]
    },
    "quest/q550.dat": {
        "bin": ["q550_688e8050_scp"]
    },
    "quest/q560.dat": {
        "bin": ["q560_291dbe71_scp"]
    },
    "quest/q561.dat": {
        "bin": ["q561_74b9a716_scp"]
    },
    "quest/q562.dat": {
        "bin": ["q562_e10ec9ab_scp"]
    },
    "quest/q590.dat": {
        "bin": ["q590_13ffe891_scp"]
    },
    "quest/q640.dat": {
        "bin": ["q640_ccd60068_scp"]
    },
    "quest/q650.dat": {
        "bin": ["q650_96497077_scp"]
    },
    "quest/q651.dat": {
        "bin": ["q651_87a1f20b_scp"]
    },
    "quest/q652.dat": {
        "bin": ["q652_4e20ab43_scp"]
    },
    "quest/q660.dat": {
        "bin": ["q660_f737718_scp"]
    },
    "quest/q680.dat": {
        "bin": ["q680_51d704e4_scp"]
    },
    "quest/q720.dat": {
        "bin": ["q720_bbe0d32e_scp"]
    },
    "quest/q770.dat": {
        "bin": ["q770_59f68d25_scp"]
    },
    "quest/q800.dat": {
        "bin": ["q800_bc7a2755_scp"]
    },
    "quest/q801.dat": {
        "bin": ["q801_6c8f629a_scp"]
    },
    "quest/q900.dat": {
        "bin": ["q900_626a2689_scp"]
    },
    "quest/q910.dat": {
        "bin": ["q910_8d8ebfae_scp"]
    },
    "quest/q920.dat": {
        "bin": ["q920_e5072c9_scp"]
    },
    "quest/qab2.dat": {
        "bin": ["qab2_aec178b7_scp"]
    },
    "quest/qab3.dat": {
        "bin": ["qab3_934fd3b1_scp"]
    },
    "quest/qab5.dat": {
        "bin": ["qab5_4a1ea1bc_scp"]
    },
    "quest/qab6.dat": {
        "bin": ["qab6_69325679_scp"]
    },
    "quest/qaba.dat": {
        "bin": ["qaba_a7ed1850_scp"]
    },
    "quest/qabb.dat": {
        "bin": ["qabb_1e5a233e_scp"]
    },
    "quest/qabd.dat": {
        "bin": ["qabd_18ca8961_scp"]
    },
    "quest/qac8.dat": {
        "bin": ["qac8_fd8ac7ea_scp"]
    },
    "quest/qad0.dat": {
        "bin": ["qad0_c493efec_scp"]
    },
    "quest/qad1.dat": {
        "bin": ["qad1_55fcb9b3_scp"]
    },
    "quest/qad2.dat": {
        "bin": ["qad2_e6ef8eaf_scp"]
    },
    "quest/qad6.dat": {
        "bin": ["qad6_b6255483_scp"]
    },
    "quest/qaeb.dat": {
        "bin": ["qaeb_98b8e891_scp"]
    },
    "quest/qaef.dat": {
        "bin": ["qaef_10112854_scp"]
    },
    "quest/qaf4.dat": {
        "bin": ["qaf4_e04e13b1_scp"]
    },
    "quest/qb20.dat": {
        "bin": [
            "qb20_42c8efa_scp",
            "qb20_91cf1fa5_scp",
        ]
    },
    "quest/qb40.dat": {
        "bin": [
            "qb40_f2a5ded9_scp",
            "qb40_b490bdc_scp",
            "qb40_ff6d92e9_scp",
            "qb40_9403a9bc_scp",
            "qb40_f7708d83_scp",
        ]
    },
    "quest/qc10.dat": {
        "bin": ["qc10_ea55109b_scp"]
    },
    "quest/qc11.dat": {
        "bin": ["qc11_e05e7f97_scp"]
    },
    "quest/qc12.dat": {
        "bin": ["qc12_9b9e9b86_scp"]
    },
    "quest/qc30.dat": {
        "bin": ["qc30_fde14379_scp"]
    },
    "quest/qc50.dat": {
        "bin": ["qc50_de375136_scp"]
    },
    "st1/r100.dat": {
        "bin": ["r100_c723351a_scp"]
    },
    "st1/r110.dat": {
        "bin": [
            "r110_be7ebe38_scp",
            "r110_6b1cbecb_scp",
            "r110_4ebc3b22_scp",
            "r110_7fe2a715_scp",
            "r110_7a562cb9_scp",
            "r110_dd7422a2_scp",
        ]
    },
    "st1/r120.dat": {
        "bin": ["r120_f0d26b5d_scp"]
    },
    "st1/r130.dat": {
        "bin": [
            "r130_e5cfdb23_scp", 
            "r130_12b5a85a_scp",
        ]
    },
    "st1/r140.dat": {
        "bin": [
            "r140_29cb90b_scp", 
            "r140_60377331_scp", 
            "r140_82d2caac_scp", 
            "r140_cd4fd96a_scp", 
            "r140_f82d8b66_scp", 
            "r140_657c1219_scp", 
            "r140_7e0bd84f_scp", 
            "r140_9fbdc6a2_scp", 
            "r140_dc76121c_scp", 
            "r140_ea0da2aa_scp", 
            "r140_336c5af9_scp", 
            "r140_49e73635_scp",
        ]
    },
    "st1/r150.dat": {
        "bin": [
            "r150_5ced6cf8_scp", 
            "r150_f100866e_scp", 
            "r150_df579346_scp",
        ]
    },
    "st1/r160.dat": {
        "bin": [
            "r160_3fa0647a_scp", 
            "r160_74d9b777_scp", 
            "r160_1557ce81_scp", 
            "r160_7247f0a7_scp", 
            "r160_307c8a44_scp", 
            "r160_f8f21cd2_scp", 
            "r160_19656865_scp", 
            "r160_e290faf0_scp", 
            "r160_dc20cee5_scp", 
            "r160_441c44e3_scp", 
            "r160_7cde1b3f_scp",
        ]
    },
    "st1/r170.dat": {
        "bin": [
            "r170_e7cef294_scp", 
            "r170_261956fa_scp",
        ]
    },
    "st2/r200.dat": {
        "bin": [
            "r200_427ea0a7_scp", 
            "r200_d52e3bf5_scp", 
            "r200_e684ee2d_scp", 
            "r200_c832af28_scp", 
            "r200_d4dad831_scp",
        ]
    },
    "st5/r530.dat": {
        "bin": ["r530_3c8107d_scp"]
    },
    f"subtitle/subtitle0010{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0010"]
    },
    f"subtitle/subtitle0011{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0011"]
    },
    f"subtitle/subtitle0030{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0030"]
    },
    f"subtitle/subtitle0031{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0031"]
    },
    f"subtitle/subtitle0040{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0040"]
    },
    f"subtitle/subtitle0050{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0050"]
    },
    f"subtitle/subtitle0055{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0055"]
    },
    f"subtitle/subtitle0060{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0060"]
    },
    f"subtitle/subtitle0080{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0080"]
    },
    f"subtitle/subtitle0081{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0081"]
    },
    f"subtitle/subtitle0086{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0086"]
    },
    f"subtitle/subtitle0090{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0090"]
    },
    f"subtitle/subtitle0091{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0091"]
    },
    f"subtitle/subtitle0092{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0092"]
    },
    f"subtitle/subtitle0110{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0110"]
    },
    f"subtitle/subtitle0111{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0111"]
    },
    f"subtitle/subtitle0120{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0120"]
    },
    f"subtitle/subtitle0130{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0130"]
    },
    f"subtitle/subtitle0140{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0140"]
    },
    f"subtitle/subtitle0160{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0160"]
    },
    f"subtitle/subtitle0170{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0170"]
    },
    f"subtitle/subtitle0190{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0190"]
    },
    f"subtitle/subtitle0191{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0191"]
    },
    f"subtitle/subtitle0225{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0225"]
    },
    f"subtitle/subtitle0226{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0226"]
    },
    f"subtitle/subtitle0230{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0230"]
    },
    f"subtitle/subtitle0240{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0240"]
    },
    f"subtitle/subtitle0241{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0241"]
    },
    f"subtitle/subtitle0250{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0250"]
    },
    f"subtitle/subtitle0251{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0251"]
    },
    f"subtitle/subtitle0260{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0260"]
    },
    f"subtitle/subtitle0262{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0262"]
    },
    f"subtitle/subtitle0270{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0270"]
    },
    f"subtitle/subtitle0280{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0280"]
    },
    f"subtitle/subtitle0300{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0300"]
    },
    f"subtitle/subtitle0301{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0301"]
    },
    f"subtitle/subtitle0310{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0310"]
    },
    f"subtitle/subtitle0311{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0311"]
    },
    f"subtitle/subtitle0320{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0320"]
    },
    f"subtitle/subtitle0321{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0321"]
    },
    f"subtitle/subtitle0322{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0322"]
    },
    f"subtitle/subtitle0323{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0323"]
    },
    f"subtitle/subtitle0325{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0325"]
    },
    f"subtitle/subtitle0326{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0326"]
    },
    f"subtitle/subtitle0330{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0330"]
    },
    f"subtitle/subtitle0340{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0340"]
    },
    f"subtitle/subtitle0341{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0341"]
    },
    f"subtitle/subtitle0350{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0350"]
    },
    f"subtitle/subtitle0351{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0351"]
    },
    f"subtitle/subtitle0352{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0352"]
    },
    f"subtitle/subtitle0360{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0360"]
    },
    f"subtitle/subtitle0370{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0370"]
    },
    f"subtitle/subtitle0390{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0390"]
    },
    f"subtitle/subtitle0400{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0400"]
    },
    f"subtitle/subtitle0410{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0410"]
    },
    f"subtitle/subtitle0420{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0420"]
    },
    f"subtitle/subtitle0440{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0440"]
    },
    f"subtitle/subtitle0441{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0441"]
    },
    f"subtitle/subtitle0460{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0460"]
    },
    f"subtitle/subtitle0461{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0461"]
    },
    f"subtitle/subtitle0470{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0470"]
    },
    f"subtitle/subtitle0471{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0471"]
    },
    f"subtitle/subtitle0475{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0475"]
    },
    f"subtitle/subtitle0480{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0480"]
    },
    f"subtitle/subtitle0482{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0482"]
    },
    f"subtitle/subtitle0483{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0483"]
    },
    f"subtitle/subtitle0485{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0485"]
    },
    f"subtitle/subtitle0490{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0490"]
    },
    f"subtitle/subtitle0491{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0491"]
    },
    f"subtitle/subtitle0500{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0500"]
    },
    f"subtitle/subtitle0502{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0502"]
    },
    f"subtitle/subtitle0520{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0520"]
    },
    f"subtitle/subtitle0521{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0521"]
    },
    f"subtitle/subtitle0525{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0525"]
    },
    f"subtitle/subtitle0526{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0526"]
    },
    f"subtitle/subtitle0530{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0530"]
    },
    f"subtitle/subtitle0531{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0531"]
    },
    f"subtitle/subtitle0540{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0540"]
    },
    f"subtitle/subtitle0550{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0550"]
    },
    f"subtitle/subtitle0552{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0552"]
    },
    f"subtitle/subtitle0570{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0570"]
    },
    f"subtitle/subtitle0571{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0571"]
    },
    f"subtitle/subtitle0590{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0590"]
    },
    f"subtitle/subtitle0600{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0600"]
    },
    f"subtitle/subtitle0610{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0610"]
    },
    f"subtitle/subtitle0612{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0612"]
    },
    f"subtitle/subtitle0630{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0630"]
    },
    f"subtitle/subtitle0631{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0631"]
    },
    f"subtitle/subtitle0640{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0640"]
    },
    f"subtitle/subtitle0642{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0642"]
    },
    f"subtitle/subtitle0650{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0650"]
    },
    f"subtitle/subtitle0651{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0651"]
    },
    f"subtitle/subtitle0655{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0655"]
    },
    f"subtitle/subtitle0656{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0656"]
    },
    f"subtitle/subtitle0660{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0660"]
    },
    f"subtitle/subtitle0661{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0661"]
    },
    f"subtitle/subtitle0670{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0670"]
    },
    f"subtitle/subtitle0671{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0671"]
    },
    f"subtitle/subtitle0680{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0680"]
    },
    f"subtitle/subtitle0682{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0682"]
    },
    f"subtitle/subtitle0690{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0690"]
    },
    f"subtitle/subtitle0692{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0692"]
    },
    f"subtitle/subtitle0693{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0693"]
    },
    f"subtitle/subtitle0694{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0694"]
    },
    f"subtitle/subtitle0700{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0700"]
    },
    f"subtitle/subtitle0702{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0702"]
    },
    f"subtitle/subtitle0720{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0720"]
    },
    f"subtitle/subtitle0722{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0722"]
    },
    f"subtitle/subtitle0730{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0730"]
    },
    f"subtitle/subtitle0760{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0760"]
    },
    f"subtitle/subtitle0761{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0761"]
    },
    f"subtitle/subtitle0770{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0770"]
    },
    f"subtitle/subtitle0771{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0771"]
    },
    f"subtitle/subtitle0780{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0780"]
    },
    f"subtitle/subtitle0781{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0781"]
    },
    f"subtitle/subtitle0790{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0790"]
    },
    f"subtitle/subtitle0791{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0791"]
    },
    f"subtitle/subtitle0792{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0792"]
    },
    f"subtitle/subtitle0800{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0800"]
    },
    f"subtitle/subtitle0810{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0810"]
    },
    f"subtitle/subtitle0811{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0811"]
    },
    f"subtitle/subtitle0820{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0820"]
    },
    f"subtitle/subtitle0830{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0830"]
    },
    f"subtitle/subtitle0835{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0835"]
    },
    f"subtitle/subtitle0836{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0836"]
    },
    f"subtitle/subtitle0850{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0850"]
    },
    f"subtitle/subtitle0855{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0855"]
    },
    f"subtitle/subtitle0860{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0860"]
    },
    f"subtitle/subtitle0861{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0861"]
    },
    f"subtitle/subtitle0870{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0870"]
    },
    f"subtitle/subtitle0871{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0871"]
    },
    f"subtitle/subtitle0875{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0875"]
    },
    f"subtitle/subtitle0880{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0880"]
    },
    f"subtitle/subtitle0900{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0900"]
    },
    f"subtitle/subtitle0901{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0901"]
    },
    f"subtitle/subtitle0910{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0910"]
    },
    f"subtitle/subtitle0920{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0920"]
    },
    f"subtitle/subtitle0921{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0921"]
    },
    f"subtitle/subtitle0926{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0926"]
    },
    f"subtitle/subtitle0930{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0930"]
    },
    f"subtitle/subtitle0931{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0931"]
    },
    f"subtitle/subtitle0935{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0935"]
    },
    f"subtitle/subtitle0936{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0936"]
    },
    f"subtitle/subtitle0940{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0940"]
    },
    f"subtitle/subtitle0950{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0950"]
    },
    f"subtitle/subtitle0951{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0951"]
    },
    f"subtitle/subtitle0960{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0960"]
    },
    f"subtitle/subtitle0961{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0961"]
    },
    f"subtitle/subtitle0970{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0970"]
    },
    f"subtitle/subtitle0990{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle0990"]
    },
    f"subtitle/subtitle1000{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1000"]
    },
    f"subtitle/subtitle1001{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1001"]
    },
    f"subtitle/subtitle1010{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1010"]
    },
    f"subtitle/subtitle1030{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1030"]
    },
    f"subtitle/subtitle1040{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1040"]
    },
    f"subtitle/subtitle1041{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1041"]
    },
    f"subtitle/subtitle1050{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1050"]
    },
    f"subtitle/subtitle1051{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1051"]
    },
    f"subtitle/subtitle1060{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1060"]
    },
    f"subtitle/subtitle1080{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1080"]
    },
    f"subtitle/subtitle1090{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1090"]
    },
    f"subtitle/subtitle1091{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1091"]
    },
    f"subtitle/subtitle1100{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1100"]
    },
    f"subtitle/subtitle1120{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1120"]
    },
    f"subtitle/subtitle1121{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1121"]
    },
    f"subtitle/subtitle1125{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1125"]
    },
    f"subtitle/subtitle1150{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1150"]
    },
    f"subtitle/subtitle1160{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1160"]
    },
    f"subtitle/subtitle1180{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1180"]
    },
    f"subtitle/subtitle1181{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1181"]
    },
    f"subtitle/subtitle1190{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1190"]
    },
    f"subtitle/subtitle1191{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1191"]
    },
    f"subtitle/subtitle1210{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1210"]
    },
    f"subtitle/subtitle1211{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1211"]
    },
    f"subtitle/subtitle1220{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1220"]
    },
    f"subtitle/subtitle1221{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1221"]
    },
    f"subtitle/subtitle1230{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1230"]
    },
    f"subtitle/subtitle1232{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1232"]
    },
    f"subtitle/subtitle1233{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1233"]
    },
    f"subtitle/subtitle1234{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1234"]
    },
    f"subtitle/subtitle1235{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1235"]
    },
    f"subtitle/subtitle1240{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1240"]
    },
    f"subtitle/subtitle1241{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1241"]
    },
    f"subtitle/subtitle1250{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1250"]
    },
    f"subtitle/subtitle1260{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1260"]
    },
    f"subtitle/subtitle1270{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1270"]
    },
    f"subtitle/subtitle1280{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1280"]
    },
    f"subtitle/subtitle1290{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1290"]
    },
    f"subtitle/subtitle1300{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1300"]
    },
    f"subtitle/subtitle1310{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1310"]
    },
    f"subtitle/subtitle1320{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1320"]
    },
    f"subtitle/subtitle1400{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1400"]
    },
    f"subtitle/subtitle1402{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitle1402"]
    },
    f"subtitle/subtitleb060{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb060"]
    },
    f"subtitle/subtitleb191{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb191"]
    },
    f"subtitle/subtitleb251{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb251"]
    },
    f"subtitle/subtitleb301{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb301"]
    },
    f"subtitle/subtitleb311{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb311"]
    },
    f"subtitle/subtitleb321{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb321"]
    },
    f"subtitle/subtitleb341{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb341"]
    },
    f"subtitle/subtitleb351{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb351"]
    },
    f"subtitle/subtitleb441{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb441"]
    },
    f"subtitle/subtitleb461{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb461"]
    },
    f"subtitle/subtitleb471{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb471"]
    },
    f"subtitle/subtitleb651{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb651"]
    },
    f"subtitle/subtitleb656{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb656"]
    },
    f"subtitle/subtitleb661{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb661"]
    },
    f"subtitle/subtitleb671{langFormats[srcLang]["default"]}.dat": {
        "smd": ["subtitleb671"]
    },
    f"txtmess/txt_chapter{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_chapter"]
    },
    f"txtmess/txt_core_add{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_core_add"]
    },
    f"txtmess/txt_core{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_core"]
    },
    f"txtmess/txt_credit{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_credit"]
    },
    f"txtmess/txt_dlc1{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_dlc1"]
    },
    f"txtmess/txt_dlc2{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_dlc2"]
    },
    f"txtmess/txt_dlc3{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_dlc3"]
    },
    f"txtmess/txt_hud_add{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_hud_add"]
    },
    f"txtmess/txt_hud{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_hud"]
    },
    f"txtmess/txt_pause_add{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_pause_add"]
    },
    f"txtmess/txt_pause{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_pause"]
    },
    f"txtmess/txt_shop{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_shop"]
    },
    f"txtmess/txt_support{langFormats[srcLang]["default"]}.dat": {
        "tmd": ["txt_support"]
    },
    f"ui/ui_chapter{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messchapter"]
    },
    f"ui/ui_core_2{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messcore_2"]
    },
    f"ui/ui_core_pc{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messcore_pc"]
    },
    f"ui/ui_core{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messcore"]
    },
    f"ui/ui_credit{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messcredit"]
    },
    f"ui/ui_dbg{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messdbg"]
    },
    f"ui/ui_dlc1{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messdlc1"]
    },
    f"ui/ui_dlc2{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messdlc2"]
    },
    f"ui/ui_dlc3{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messdlc3"]
    },
    f"ui/ui_ending_dlc{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messending_dlc"]
    },
    f"ui/ui_ending{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messending"]
    },
    f"ui/ui_event{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messevent"]
    },
    f"ui/ui_hud_hacking{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messhud_hacking"]
    },
    f"ui/ui_hud{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messhud"]
    },
    f"ui/ui_loading.dat": {
        "mcd": ["messloading"]
    },
    f"ui/ui_option{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messoption"]
    },
    f"ui/ui_pause{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messpause"]
    },
    f"ui/ui_shop{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messshop"]
    },
    f"ui/ui_title{langFormats[srcLang]["default"]}.dat": {
        "mcd": ["messtitle"]
    },
    "wd1/g11516.dat": {
        "bin": ["g11516_2ccba2ea_scp"]
    },
    "novel": {
        "txt": [
            f"M1030_S0310_N{langFormats[srcLang]["novel"]}", 
            f"M1070_S0020_N{langFormats[srcLang]["novel"]}", 
            f"M1070_S0040_N{langFormats[srcLang]["novel"]}", 
            f"M1070_S0060_N{langFormats[srcLang]["novel"]}", 
            f"M1070_S0080_N{langFormats[srcLang]["novel"]}", 
            f"M1070_S0100_N{langFormats[srcLang]["novel"]}", 
            f"M3060_S0005_N{langFormats[srcLang]["novel"]}", 
            f"M3060_S0035_GM_N{langFormats[srcLang]["novel"]}", 
            f"M3060_S0910_N{langFormats[srcLang]["novel"]}", 
            f"M6010_S0050_N{langFormats[srcLang]["novel"]}", 
            f"M6010_S0150_N{langFormats[srcLang]["novel"]}", 
            f"M6010_S0250_N{langFormats[srcLang]["novel"]}", 
            f"M9000_S0500_N{langFormats[srcLang]["novel"]}", 
            f"M5095_S0020_N{langFormats[srcLang]["novel"]}", 
            f"M5095_S0025_N{langFormats[srcLang]["novel"]}", 
            f"M5095_S0100_N{langFormats[srcLang]["novel"]}", 
            f"M5095_S0200_N{langFormats[srcLang]["novel"]}", 
            f"M5095_S0300_N{langFormats[srcLang]["novel"]}"
        ]
    }
}
class MyConsole(Console):
    HEADING_STYLE = "bold white on blue"

    def heading(self, text: str):
        super().rule(f"[{self.HEADING_STYLE}]{text}", style=self.HEADING_STYLE)
