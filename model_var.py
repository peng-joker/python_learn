import math

def woe_bin(var, varname):

	## WoE coding for alm_m10_cell_nbank_p2p_allnum -> walm_m10_cell_nba_num_1501_bn ##
	if varname == 'alm_m10_cell_nbank_p2p_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 1.0:
			return '101:(-Inf,1.0]'
		elif 1.0 < var <= 2.0:
			return '102:(1.0,2.0]'
		elif var > 2.0:
			return '103:(2.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for alm_m11_id_bank_orgnum -> walm_m11_id_bank_orgnum_bn ##
	if varname == 'alm_m11_id_bank_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 1.0:
			return '101:(-Inf,1.0]'
		elif 1.0 < var <= 2.0:
			return '102:(1.0,2.0]'
		elif 2.0 < var <= 4.0:
			return '103:(2.0,4.0]'
		elif 4.0 < var <= 5.0:
			return '104:(4.0,5.0]'
		elif var > 5.0:
			return '105:(5.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for alm_m3_cell_nbank_nsloan_orgnum -> walm_m3_cell_nban_num_1D07_bn ##
	if varname == 'alm_m3_cell_nbank_nsloan_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 1.0:
			return '101:(-Inf,1.0]'
		elif 1.0 < var <= 2.0:
			return '102:(1.0,2.0]'
		elif 2.0 < var <= 4.0:
			return '103:(2.0,4.0]'
		elif 4.0 < var <= 5.0:
			return '104:(4.0,5.0]'
		elif 5.0 < var <= 8.0:
			return '105:(5.0,8.0]'
		elif var > 8.0:
			return '106:(8.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for alm_m9_cell_nbank_p2p_allnum -> walm_m9_cell_nban_num_D94C_bn ##
	if varname == 'alm_m9_cell_nbank_p2p_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 2.0:
			return '101:(-Inf,2.0]'
		elif var > 2.0:
			return '102:(2.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m12_cell_nbank_selfnum -> wals_m12_cell_nba_num_BB0E_bn ##
	if varname == 'als_m12_cell_nbank_selfnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.0:
			return '101:(-Inf,0.0]'
		elif 0.0 < var <= 1.0:
			return '102:(0.0,1.0]'
		elif 1.0 < var <= 3.0:
			return '103:(1.0,3.0]'
		elif var > 3.0:
			return '104:(3.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m3_cell_caoff_allnum -> wals_m3_cell_caoff_allnum_bn ##
	if varname == 'als_m3_cell_caoff_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 1.0:
			return '101:(-Inf,1.0]'
		elif 1.0 < var <= 2.0:
			return '102:(1.0,2.0]'
		elif 2.0 < var <= 4.0:
			return '103:(2.0,4.0]'
		elif 4.0 < var <= 6.0:
			return '104:(4.0,6.0]'
		elif 6.0 < var <= 12.0:
			return '105:(6.0,12.0]'
		elif var > 12.0:
			return '106:(12.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m3_id_nbank_finlea_allnum -> wals_m3_id_nbank__num_0823_bn ##
	if varname == 'als_m3_id_nbank_finlea_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 1.0:
			return '101:(-Inf,1.0]'
		elif 1.0 < var <= 3.0:
			return '102:(1.0,3.0]'
		elif 3.0 < var <= 4.0:
			return '103:(3.0,4.0]'
		elif 4.0 < var <= 5.0:
			return '104:(4.0,5.0]'
		elif 5.0 < var <= 6.0:
			return '105:(5.0,6.0]'
		elif var > 6.0:
			return '106:(6.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m6_id_bank_min_inteday -> wals_m6_id_bank_m_day_884E_bn ##
	if varname == 'als_m6_id_bank_min_inteday':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.0:
			return '101:(-Inf,0.0]'
		elif 0.0 < var <= 1.0:
			return '102:(0.0,1.0]'
		elif 1.0 < var <= 3.0:
			return '103:(1.0,3.0]'
		elif 3.0 < var <= 12.0:
			return '104:(3.0,12.0]'
		elif 12.0 < var <= 21.0:
			return '105:(12.0,21.0]'
		elif var > 21.0:
			return '106:(21.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m6_id_caoff_orgnum -> wals_m6_id_caoff_orgnum_bn ##
	if varname == 'als_m6_id_caoff_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 1.0:
			return '101:(-Inf,1.0]'
		elif 1.0 < var <= 2.0:
			return '102:(1.0,2.0]'
		elif 2.0 < var <= 3.0:
			return '103:(2.0,3.0]'
		elif 3.0 < var <= 4.0:
			return '104:(3.0,4.0]'
		elif 4.0 < var <= 5.0:
			return '105:(4.0,5.0]'
		elif var > 5.0:
			return '106:(5.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m6_id_caon_allnum -> wals_m6_id_caon_allnum_bn ##
	if varname == 'als_m6_id_caon_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 10.0:
			return '101:(-Inf,10.0]'
		elif 10.0 < var <= 19.0:
			return '102:(10.0,19.0]'
		elif 19.0 < var <= 62.0:
			return '103:(19.0,62.0]'
		elif 62.0 < var <= 71.0:
			return '104:(62.0,71.0]'
		elif 71.0 < var <= 84.0:
			return '105:(71.0,84.0]'
		elif var > 84.0:
			return '106:(84.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m6_id_nbank_finlea_orgnum -> wals_m6_id_nbank__num_2554_bn ##
	if varname == 'als_m6_id_nbank_finlea_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 1.0:
			return '101:(-Inf,1.0]'
		elif 1.0 < var <= 2.0:
			return '102:(1.0,2.0]'
		elif 2.0 < var <= 3.0:
			return '103:(2.0,3.0]'
		elif var > 3.0:
			return '104:(3.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for als_m6_id_rel_allnum -> wals_m6_id_rel_allnum_bn ##
	if varname == 'als_m6_id_rel_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 2.0:
			return '101:(-Inf,2.0]'
		elif 2.0 < var <= 3.0:
			return '102:(2.0,3.0]'
		elif 3.0 < var <= 5.0:
			return '103:(3.0,5.0]'
		elif 5.0 < var <= 7.0:
			return '104:(5.0,7.0]'
		elif 7.0 < var <= 11.0:
			return '105:(7.0,11.0]'
		elif 11.0 < var <= 12.0:
			return '106:(11.0,12.0]'
		elif 12.0 < var <= 15.0:
			return '107:(12.0,15.0]'
		elif 15.0 < var <= 17.0:
			return '108:(15.0,17.0]'
		elif var > 17.0:
			return '109:(17.0,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_d15_cell_nbank_else_rel_allnum -> wql_d15_cell_nban_num_4135_bn ##
	if varname == 'ql_d15_cell_nbank_else_rel_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9954:
			return '101:(-Inf,0.9954]'
		elif 0.9954 < var <= 0.9961:
			return '102:(0.9954,0.9961]'
		elif var > 0.9961:
			return '103:(0.9961,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_d15_cell_nbank_sloan_orgnum -> wql_d15_cell_nban_num_FB7E_bn ##
	if varname == 'ql_d15_cell_nbank_sloan_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9981:
			return '101:(-Inf,0.9981]'
		elif 0.9981 < var <= 0.9982:
			return '102:(0.9981,0.9982]'
		elif 0.9982 < var <= 0.9983:
			return '103:(0.9982,0.9983]'
		elif 0.9983 < var <= 0.9984:
			return '104:(0.9983,0.9984]'
		elif var > 0.9984:
			return '105:(0.9984,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_d15_id_nbank_else_pdl_orgnum -> wql_d15_id_nbank__num_671A_bn ##
	if varname == 'ql_d15_id_nbank_else_pdl_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9886:
			return '101:(-Inf,0.9886]'
		elif 0.9886 < var <= 0.9997:
			return '102:(0.9886,0.9997]'
		elif var > 0.9997:
			return '103:(0.9997,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_d15_id_nbank_night_allnum -> wql_d15_id_nbank__num_6B76_bn ##
	if varname == 'ql_d15_id_nbank_night_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9664:
			return '101:(-Inf,0.9664]'
		elif 0.9664 < var <= 0.9692:
			return '102:(0.9664,0.9692]'
		elif 0.9692 < var <= 0.9752:
			return '103:(0.9692,0.9752]'
		elif 0.9752 < var <= 0.9956:
			return '104:(0.9752,0.9956]'
		elif var > 0.9956:
			return '105:(0.9956,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_d3_cell_nbank_else_rel_orgnum -> wql_d3_cell_nbank_num_DAE2_bn ##
	if varname == 'ql_d3_cell_nbank_else_rel_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9991:
			return '101:(-Inf,0.9991]'
		elif 0.9991 < var <= 0.9992:
			return '102:(0.9991,0.9992]'
		elif var > 0.9992:
			return '103:(0.9992,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_d7_cell_nbank_top_orgnum -> wql_d7_cell_nbank_num_753C_bn ##
	if varname == 'ql_d7_cell_nbank_top_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.8872:
			return '101:(-Inf,0.8872]'
		elif 0.8872 < var <= 0.8962:
			return '102:(0.8872,0.8962]'
		elif 0.8962 < var <= 0.9255:
			return '103:(0.8962,0.9255]'
		elif 0.9255 < var <= 0.9957:
			return '104:(0.9255,0.9957]'
		elif var > 0.9957:
			return '105:(0.9957,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m12_cell_min_monnum -> wql_m12_cell_min_monnum_bn ##
	if varname == 'ql_m12_cell_min_monnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.4593:
			return '101:(-Inf,0.4593]'
		elif 0.4593 < var <= 0.4631:
			return '102:(0.4593,0.4631]'
		elif var > 0.4631:
			return '103:(0.4631,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m12_cell_nbank_autofin_orgnum -> wql_m12_cell_nban_num_9AEF_bn ##
	if varname == 'ql_m12_cell_nbank_autofin_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9783:
			return '101:(-Inf,0.9783]'
		elif 0.9783 < var <= 0.9801:
			return '102:(0.9783,0.9801]'
		elif 0.9801 < var <= 0.9805:
			return '103:(0.9801,0.9805]'
		elif 0.9805 < var <= 0.9807:
			return '104:(0.9805,0.9807]'
		elif var > 0.9807:
			return '105:(0.9807,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m12_cell_nbank_night_orgnum -> wql_m12_cell_nban_num_7DC2_bn ##
	if varname == 'ql_m12_cell_nbank_night_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.4891:
			return '101:(-Inf,0.4891]'
		elif 0.4891 < var <= 0.9934:
			return '102:(0.4891,0.9934]'
		elif var > 0.9934:
			return '103:(0.9934,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m12_cell_nbank_trans_orgnum -> wql_m12_cell_nban_num_173E_bn ##
	if varname == 'ql_m12_cell_nbank_trans_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9623:
			return '101:(-Inf,0.9623]'
		elif 0.9623 < var <= 0.9625:
			return '102:(0.9623,0.9625]'
		elif 0.9625 < var <= 0.9644:
			return '103:(0.9625,0.9644]'
		elif 0.9644 < var <= 0.9663:
			return '104:(0.9644,0.9663]'
		elif var > 0.9663:
			return '105:(0.9663,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m12_id_nbank_ins_orgnum -> wql_m12_id_nbank__num_D894_bn ##
	if varname == 'ql_m12_id_nbank_ins_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.8669:
			return '101:(-Inf,0.8669]'
		elif 0.8669 < var <= 0.889:
			return '102:(0.8669,0.889]'
		elif 0.889 < var <= 0.8963:
			return '103:(0.889,0.8963]'
		elif 0.8963 < var <= 0.9029:
			return '104:(0.8963,0.9029]'
		elif 0.9029 < var <= 0.9109:
			return '105:(0.9029,0.9109]'
		elif 0.9109 < var <= 0.9922:
			return '106:(0.9109,0.9922]'
		elif var > 0.9922:
			return '107:(0.9922,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m3_cell_nbank_cons_orgnum -> wql_m3_cell_nbank_num_45EA_bn ##
	if varname == 'ql_m3_cell_nbank_cons_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.8875:
			return '101:(-Inf,0.8875]'
		elif 0.8875 < var <= 0.996:
			return '102:(0.8875,0.996]'
		elif 0.996 < var <= 0.9997:
			return '103:(0.996,0.9997]'
		elif var > 0.9997:
			return '104:(0.9997,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m3_cell_nbank_sloan_allnum -> wql_m3_cell_nbank_num_5E79_bn ##
	if varname == 'ql_m3_cell_nbank_sloan_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9974:
			return '101:(-Inf,0.9974]'
		elif 0.9974 < var <= 0.9998:
			return '102:(0.9974,0.9998]'
		elif var > 0.9998:
			return '103:(0.9998,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m3_cell_nbank_trans_orgnum -> wql_m3_cell_nbank_num_8CF1_bn ##
	if varname == 'ql_m3_cell_nbank_trans_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.983:
			return '101:(-Inf,0.983]'
		elif 0.983 < var <= 0.984:
			return '102:(0.983,0.984]'
		elif 0.984 < var <= 0.9841:
			return '103:(0.984,0.9841]'
		elif 0.9841 < var <= 0.9845:
			return '104:(0.9841,0.9845]'
		elif var > 0.9845:
			return '105:(0.9845,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m3_id_nbank_cons_allnum -> wql_m3_id_nbank_c_num_3BF3_bn ##
	if varname == 'ql_m3_id_nbank_cons_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.8758:
			return '101:(-Inf,0.8758]'
		elif 0.8758 < var <= 0.977:
			return '102:(0.8758,0.977]'
		elif 0.977 < var <= 0.9928:
			return '103:(0.977,0.9928]'
		elif 0.9928 < var <= 0.9954:
			return '104:(0.9928,0.9954]'
		elif 0.9954 < var <= 0.9977:
			return '105:(0.9954,0.9977]'
		elif 0.9977 < var <= 0.9995:
			return '106:(0.9977,0.9995]'
		elif var > 0.9995:
			return '107:(0.9995,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m3_id_nbank_else_rel_orgnum -> wql_m3_id_nbank_e_num_25D5_bn ##
	if varname == 'ql_m3_id_nbank_else_rel_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9686:
			return '101:(-Inf,0.9686]'
		elif 0.9686 < var <= 0.9687:
			return '102:(0.9686,0.9687]'
		elif 0.9687 < var <= 0.9998:
			return '103:(0.9687,0.9998]'
		elif var > 0.9998:
			return '104:(0.9998,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m3_id_nbank_sloan_allnum -> wql_m3_id_nbank_s_num_92CA_bn ##
	if varname == 'ql_m3_id_nbank_sloan_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9868:
			return '101:(-Inf,0.9868]'
		elif 0.9868 < var <= 0.9954:
			return '102:(0.9868,0.9954]'
		elif 0.9954 < var <= 0.9985:
			return '103:(0.9954,0.9985]'
		elif 0.9985 < var <= 0.9997:
			return '104:(0.9985,0.9997]'
		elif var > 0.9997:
			return '105:(0.9997,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m6_cell_bank_min_monnum -> wql_m6_cell_bank__num_753A_bn ##
	if varname == 'ql_m6_cell_bank_min_monnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.7128:
			return '101:(-Inf,0.7128]'
		elif 0.7128 < var <= 0.7224:
			return '102:(0.7128,0.7224]'
		elif 0.7224 < var <= 0.732:
			return '103:(0.7224,0.732]'
		elif 0.732 < var <= 0.9588:
			return '104:(0.732,0.9588]'
		elif var > 0.9588:
			return '105:(0.9588,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m6_cell_bank_night_orgnum -> wql_m6_cell_bank__num_A70B_bn ##
	if varname == 'ql_m6_cell_bank_night_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9402:
			return '101:(-Inf,0.9402]'
		elif 0.9402 < var <= 0.9413:
			return '102:(0.9402,0.9413]'
		elif 0.9413 < var <= 0.9429:
			return '103:(0.9413,0.9429]'
		elif var > 0.9429:
			return '104:(0.9429,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m6_cell_nbank_else_rel_allnum -> wql_m6_cell_nbank_num_47D2_bn ##
	if varname == 'ql_m6_cell_nbank_else_rel_allnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9983:
			return '101:(-Inf,0.9983]'
		elif 0.9983 < var <= 0.9993:
			return '102:(0.9983,0.9993]'
		elif 0.9993 < var <= 0.9995:
			return '103:(0.9993,0.9995]'
		elif 0.9995 < var <= 0.9997:
			return '104:(0.9995,0.9997]'
		elif 0.9997 < var <= 0.9998:
			return '105:(0.9997,0.9998]'
		elif var > 0.9998:
			return '106:(0.9998,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m6_id_bank_tot_mons -> wql_m6_id_bank_tot_mons_bn ##
	if varname == 'ql_m6_id_bank_tot_mons':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9093:
			return '101:(-Inf,0.9093]'
		elif 0.9093 < var <= 0.9538:
			return '102:(0.9093,0.9538]'
		elif 0.9538 < var <= 0.9796:
			return '103:(0.9538,0.9796]'
		elif var > 0.9796:
			return '104:(0.9796,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m6_id_nbank_else_rel_orgnum -> wql_m6_id_nbank_e_num_5CCA_bn ##
	if varname == 'ql_m6_id_nbank_else_rel_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.9884:
			return '101:(-Inf,0.9884]'
		elif 0.9884 < var <= 0.9963:
			return '102:(0.9884,0.9963]'
		elif 0.9963 < var <= 0.9987:
			return '103:(0.9963,0.9987]'
		elif 0.9987 < var <= 0.9989:
			return '104:(0.9987,0.9989]'
		elif 0.9989 < var <= 0.9997:
			return '105:(0.9989,0.9997]'
		elif var > 0.9997:
			return '106:(0.9997,+Inf)'
		else:
			return '999:Else'


	## WoE coding for ql_m6_id_nbank_night_orgnum -> wql_m6_id_nbank_n_num_4E94_bn ##
	if varname == 'ql_m6_id_nbank_night_orgnum':
		if math.isnan(var):
			return '100:NULL'
		elif -100000000.0 < var <= 0.8365:
			return '101:(-Inf,0.8365]'
		elif 0.8365 < var <= 0.8424:
			return '102:(0.8365,0.8424]'
		elif 0.8424 < var <= 0.9537:
			return '103:(0.8424,0.9537]'
		elif var > 0.9537:
			return '104:(0.9537,+Inf)'
		else:
			return '999:Else'



