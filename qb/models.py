# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Blocknames(models.Model):
    block_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blocknames'


class CommonSchoolFacilityIn15And16(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    bldstatus = models.CharField(max_length=2, blank=True, null=True)
    clrooms = models.CharField(max_length=3, blank=True, null=True)
    clgood = models.CharField(max_length=3, blank=True, null=True)
    clmajor = models.CharField(max_length=2, blank=True, null=True)
    clminor = models.CharField(max_length=2, blank=True, null=True)
    toiletb = models.CharField(max_length=3, blank=True, null=True)
    toilet_g = models.CharField(max_length=3, blank=True, null=True)
    mealsinsch = models.CharField(max_length=2, blank=True, null=True)
    cal_yn = models.CharField(max_length=2, blank=True, null=True)
    hmroom_yn = models.CharField(max_length=2, blank=True, null=True)
    electric_yn = models.CharField(max_length=2, blank=True, null=True)
    bndrywall = models.CharField(max_length=2, blank=True, null=True)
    library_yn = models.CharField(max_length=2, blank=True, null=True)
    pground_yn = models.CharField(max_length=2, blank=True, null=True)
    bookinlib = models.CharField(max_length=6, blank=True, null=True)
    water = models.CharField(max_length=2, blank=True, null=True)
    medchk_yn = models.CharField(max_length=2, blank=True, null=True)
    ramps_yn = models.CharField(max_length=2, blank=True, null=True)
    computer = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_school_facility_in_15_and_16'


class DistrictTaluka(models.Model):
    district_name_2011 = models.CharField(max_length=30, blank=True, null=True)
    district_name_2017 = models.CharField(max_length=30, blank=True, null=True)
    district_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    district_code_2011 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taluka_name_lg = models.CharField(max_length=30, blank=True, null=True)
    taluka_code_2011 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taluka_name_2011 = models.CharField(max_length=30, blank=True, null=True)
    taluka_code_lg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_taluka'


class FaultyPincodes(models.Model):
    distname = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    school_name = models.CharField(max_length=300, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    cluster_name = models.CharField(max_length=100, blank=True, null=True)
    village_name = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'faulty_pincodes'


class Layer(models.Model):
    topology = models.OneToOneField('Topology', models.DO_NOTHING, primary_key=True)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=20)
    table_name = models.CharField(max_length=20)
    feature_column = models.CharField(max_length=20)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class Maha(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    district_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taluka_code_2011 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    census_201 = models.CharField(max_length=6, blank=True, null=True)
    ward = models.CharField(max_length=4, blank=True, null=True)
    area_name = models.CharField(max_length=60, blank=True, null=True)
    tru = models.CharField(max_length=20, blank=True, null=True)
    no_hh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_06 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_06 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f_06 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_sc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_sc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f_sc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_st = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_st = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f_st = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_lit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_lit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f_lit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p_ill = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    m_ill = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    f_ill = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_work_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_work_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_work_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mainwork_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mainwork_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mainwork_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_cl_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_cl_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_cl_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_al_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_al_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_al_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_hh_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_hh_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_hh_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_ot_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_ot_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    main_ot_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_cl_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_cl_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_cl_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_al_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_al_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_al_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_hh_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_hh_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_hh_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_ot_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_ot_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_ot_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_cl_3_field = models.DecimalField(db_column='marg_cl_3_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_1 = models.DecimalField(db_column='marg_cl__1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_2 = models.DecimalField(db_column='marg_cl__2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_3_field = models.DecimalField(db_column='marg_al_3_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_1 = models.DecimalField(db_column='marg_al__1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_2 = models.DecimalField(db_column='marg_al__2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_3_field = models.DecimalField(db_column='marg_hh_3_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_1 = models.DecimalField(db_column='marg_hh__1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_2 = models.DecimalField(db_column='marg_hh__2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_3_field = models.DecimalField(db_column='marg_ot_3_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_1 = models.DecimalField(db_column='marg_ot__1', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_2 = models.DecimalField(db_column='marg_ot__2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    margwork_0 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    margwork_5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    marg_cl_0_field = models.DecimalField(db_column='marg_cl_0_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_cl_3 = models.DecimalField(db_column='marg_cl__3', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_cl_4 = models.DecimalField(db_column='marg_cl__4', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_0_field = models.DecimalField(db_column='marg_al_0_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_al_3 = models.DecimalField(db_column='marg_al__3', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_al_4 = models.DecimalField(db_column='marg_al__4', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_0_field = models.DecimalField(db_column='marg_hh_0_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_hh_3 = models.DecimalField(db_column='marg_hh__3', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_hh_4 = models.DecimalField(db_column='marg_hh__4', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_0_field = models.DecimalField(db_column='marg_ot_0_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    marg_ot_3 = models.DecimalField(db_column='marg_ot__3', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    marg_ot_4 = models.DecimalField(db_column='marg_ot__4', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    non_work_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    non_work_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    non_work_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    district_name = models.CharField(max_length=50, blank=True, null=True)
    taluka_name = models.CharField(max_length=50, blank=True, null=True)
    circle_name = models.CharField(max_length=50, blank=True, null=True)
    mini_water = models.CharField(max_length=20, blank=True, null=True)
    village_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    village_name = models.CharField(max_length=50, blank=True, null=True)
    taluka_code_lg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maha'


class MahaDdw(models.Model):
    id = models.IntegerField(primary_key=True)
    district_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taluka_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    census_2011code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ward = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_name = models.CharField(max_length=20, blank=True, null=True)
    tru = models.CharField(max_length=20, blank=True, null=True)
    no_hh = models.CharField(max_length=20, blank=True, null=True)
    tot_p = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tot_m = models.CharField(max_length=20, blank=True, null=True)
    tot_f = models.CharField(max_length=20, blank=True, null=True)
    p_06 = models.CharField(max_length=20, blank=True, null=True)
    m_06 = models.CharField(max_length=20, blank=True, null=True)
    f_06 = models.CharField(max_length=20, blank=True, null=True)
    p_sc = models.CharField(max_length=20, blank=True, null=True)
    m_sc = models.CharField(max_length=20, blank=True, null=True)
    f_sc = models.CharField(max_length=20, blank=True, null=True)
    p_st = models.CharField(max_length=20, blank=True, null=True)
    m_st = models.CharField(max_length=20, blank=True, null=True)
    f_st = models.CharField(max_length=20, blank=True, null=True)
    p_lit = models.CharField(max_length=20, blank=True, null=True)
    m_lit = models.CharField(max_length=20, blank=True, null=True)
    f_lit = models.CharField(max_length=20, blank=True, null=True)
    p_ill = models.CharField(max_length=20, blank=True, null=True)
    m_ill = models.CharField(max_length=20, blank=True, null=True)
    f_ill = models.CharField(max_length=20, blank=True, null=True)
    tot_work_p = models.CharField(max_length=20, blank=True, null=True)
    tot_work_m = models.CharField(max_length=20, blank=True, null=True)
    tot_work_f = models.CharField(max_length=20, blank=True, null=True)
    mainwork_p = models.CharField(max_length=20, blank=True, null=True)
    mainwork_m = models.CharField(max_length=20, blank=True, null=True)
    mainwork_f = models.CharField(max_length=20, blank=True, null=True)
    main_cl_p = models.CharField(max_length=20, blank=True, null=True)
    main_cl_m = models.CharField(max_length=20, blank=True, null=True)
    main_cl_f = models.CharField(max_length=20, blank=True, null=True)
    main_al_p = models.CharField(max_length=20, blank=True, null=True)
    main_al_m = models.CharField(max_length=20, blank=True, null=True)
    main_al_f = models.CharField(max_length=20, blank=True, null=True)
    main_hh_p = models.CharField(max_length=20, blank=True, null=True)
    main_hh_m = models.CharField(max_length=20, blank=True, null=True)
    main_hh_f = models.CharField(max_length=20, blank=True, null=True)
    main_ot_p = models.CharField(max_length=20, blank=True, null=True)
    main_ot_m = models.CharField(max_length=20, blank=True, null=True)
    main_ot_f = models.CharField(max_length=20, blank=True, null=True)
    margwork_p = models.CharField(max_length=20, blank=True, null=True)
    margwork_m = models.CharField(max_length=20, blank=True, null=True)
    margwork_f = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_p = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_m = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_f = models.CharField(max_length=20, blank=True, null=True)
    marg_al_p = models.CharField(max_length=20, blank=True, null=True)
    marg_al_m = models.CharField(max_length=20, blank=True, null=True)
    marg_al_f = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_p = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_m = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_f = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_p = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_m = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_f = models.CharField(max_length=20, blank=True, null=True)
    margwork_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    margwork_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    margwork_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_al_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_al_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_al_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    margwork_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    margwork_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    margwork_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_al_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_al_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_al_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    non_work_p = models.CharField(max_length=20, blank=True, null=True)
    non_work_m = models.CharField(max_length=20, blank=True, null=True)
    non_work_f = models.CharField(max_length=20, blank=True, null=True)
    census2011_ward = models.CharField(max_length=100, blank=True, null=True)
    district_code2017 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maha_ddw'


class MaharashtraUrbanSchool(models.Model):
    state_code = models.CharField(max_length=2, blank=True, null=True)
    state_name = models.CharField(max_length=50, blank=True, null=True)
    district_code = models.CharField(max_length=3, blank=True, null=True)
    district_name = models.CharField(max_length=50, blank=True, null=True)
    town_code = models.CharField(max_length=8, blank=True, null=True)
    town_name = models.CharField(max_length=50, blank=True, null=True)
    ward_code = models.CharField(max_length=3, blank=True, null=True)
    school_code = models.CharField(max_length=4, blank=True, null=True)
    school_category_master_school_category_code = models.CharField(max_length=1, blank=True, null=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    school_address = models.CharField(max_length=500, blank=True, null=True)
    area = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maharashtra_urban_school'


class MergedDbToCompareLgCensus(models.Model):
    vid = models.IntegerField(primary_key=True)
    village_code = models.IntegerField(blank=True, null=True)
    vcensus_2011code = models.IntegerField(blank=True, null=True)
    lg_distname = models.CharField(max_length=20, blank=True, null=True)
    district_code_2017 = models.IntegerField(blank=True, null=True)
    district_name_2017 = models.CharField(max_length=20, blank=True, null=True)
    district_name_matches = models.CharField(max_length=20, blank=True, null=True)
    subdistrict_code = models.IntegerField(blank=True, null=True)
    taluka_code2011 = models.IntegerField(blank=True, null=True)
    subdistrict_name = models.CharField(max_length=20, blank=True, null=True)
    taluka_name = models.CharField(max_length=20, blank=True, null=True)
    taluka_name_matches = models.CharField(max_length=20, blank=True, null=True)
    lg_villagename = models.CharField(max_length=20, blank=True, null=True)
    census11_villagename = models.CharField(max_length=20, blank=True, null=True)
    village_name_matches = models.CharField(max_length=20, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    district_code = models.CharField(max_length=20, blank=True, null=True)
    taluka_code = models.CharField(max_length=20, blank=True, null=True)
    census_2011code = models.CharField(max_length=20, blank=True, null=True)
    ward = models.CharField(max_length=20, blank=True, null=True)
    area_name = models.CharField(max_length=20, blank=True, null=True)
    tru = models.CharField(max_length=20, blank=True, null=True)
    no_hh = models.CharField(max_length=20, blank=True, null=True)
    tot_p = models.CharField(max_length=20, blank=True, null=True)
    tot_m = models.CharField(max_length=20, blank=True, null=True)
    tot_f = models.CharField(max_length=20, blank=True, null=True)
    p_06 = models.CharField(max_length=20, blank=True, null=True)
    m_06 = models.CharField(max_length=20, blank=True, null=True)
    f_06 = models.CharField(max_length=20, blank=True, null=True)
    p_sc = models.CharField(max_length=20, blank=True, null=True)
    m_sc = models.CharField(max_length=20, blank=True, null=True)
    f_sc = models.CharField(max_length=20, blank=True, null=True)
    p_st = models.CharField(max_length=20, blank=True, null=True)
    m_st = models.CharField(max_length=20, blank=True, null=True)
    f_st = models.CharField(max_length=20, blank=True, null=True)
    p_lit = models.CharField(max_length=20, blank=True, null=True)
    m_lit = models.CharField(max_length=20, blank=True, null=True)
    f_lit = models.CharField(max_length=20, blank=True, null=True)
    p_ill = models.CharField(max_length=20, blank=True, null=True)
    m_ill = models.CharField(max_length=20, blank=True, null=True)
    f_ill = models.CharField(max_length=20, blank=True, null=True)
    tot_work_p = models.CharField(max_length=20, blank=True, null=True)
    tot_work_m = models.CharField(max_length=20, blank=True, null=True)
    tot_work_f = models.CharField(max_length=20, blank=True, null=True)
    mainwork_p = models.CharField(max_length=20, blank=True, null=True)
    mainwork_m = models.CharField(max_length=20, blank=True, null=True)
    mainwork_f = models.CharField(max_length=20, blank=True, null=True)
    main_cl_p = models.CharField(max_length=20, blank=True, null=True)
    main_cl_m = models.CharField(max_length=20, blank=True, null=True)
    main_cl_f = models.CharField(max_length=20, blank=True, null=True)
    main_al_p = models.CharField(max_length=20, blank=True, null=True)
    main_al_m = models.CharField(max_length=20, blank=True, null=True)
    main_al_f = models.CharField(max_length=20, blank=True, null=True)
    main_hh_p = models.CharField(max_length=20, blank=True, null=True)
    main_hh_m = models.CharField(max_length=20, blank=True, null=True)
    main_hh_f = models.CharField(max_length=20, blank=True, null=True)
    main_ot_p = models.CharField(max_length=20, blank=True, null=True)
    main_ot_m = models.CharField(max_length=20, blank=True, null=True)
    main_ot_f = models.CharField(max_length=20, blank=True, null=True)
    margwork_p = models.CharField(max_length=20, blank=True, null=True)
    margwork_m = models.CharField(max_length=20, blank=True, null=True)
    margwork_f = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_p = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_m = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_f = models.CharField(max_length=20, blank=True, null=True)
    marg_al_p = models.CharField(max_length=20, blank=True, null=True)
    marg_al_m = models.CharField(max_length=20, blank=True, null=True)
    marg_al_f = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_p = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_m = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_f = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_p = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_m = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_f = models.CharField(max_length=20, blank=True, null=True)
    margwork_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    margwork_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    margwork_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_al_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_al_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_al_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_3_6_p = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_3_6_m = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_3_6_f = models.CharField(max_length=20, blank=True, null=True)
    margwork_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    margwork_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    margwork_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_cl_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_al_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_al_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_al_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_hh_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_0_3_p = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_0_3_m = models.CharField(max_length=20, blank=True, null=True)
    marg_ot_0_3_f = models.CharField(max_length=20, blank=True, null=True)
    non_work_p = models.CharField(max_length=20, blank=True, null=True)
    non_work_m = models.CharField(max_length=20, blank=True, null=True)
    non_work_f = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merged_db_to_compare_lg_census'


class PalgharGeocodedLatlong(models.Model):
    school_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    school_name = models.CharField(max_length=300, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'palghar_geocoded_latlong'


class PincodesWithUrc(models.Model):
    pincode = models.CharField(max_length=6, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincodes_with_urc'


class PincodesWithoutUrc(models.Model):
    block_name = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincodes_without_urc'


class School1516(models.Model):
    distname = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    school_name = models.CharField(max_length=300, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    cluster_name = models.CharField(max_length=100, blank=True, null=True)
    village_name = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'school15_16'


class School1617(models.Model):
    distname = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    school_name = models.CharField(max_length=300, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    cluster_name = models.CharField(max_length=100, blank=True, null=True)
    village_name = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'school16_17'


class School1617Codes(models.Model):
    distname = models.CharField(max_length=100, blank=True, null=True)
    district_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    block_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cluster_name = models.CharField(max_length=100, blank=True, null=True)
    village_name = models.CharField(max_length=100, blank=True, null=True)
    village_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    school_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    school_name = models.CharField(max_length=300, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    block_name_alias = models.CharField(max_length=100, blank=True, null=True)
    ward = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    villagecode_ward = models.CharField(max_length=100, blank=True, null=True)
    village_name_alias = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school16_17_codes'



class SchoolDisableEnrolment1516(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    c1_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c1_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c2_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c2_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c3_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c3_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c4_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c4_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c5_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c5_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c6_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c6_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c7_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c7_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c8_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c8_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c9_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c9_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c10_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c10_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c11_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c11_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c12_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c12_dis_g = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_disable_enrolment_15_16'


class SchoolDisableEnrolment1617(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    c1_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c1_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c2_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c2_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c3_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c3_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c4_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c4_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c5_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c5_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c6_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c6_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c7_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c7_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c8_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c8_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c9_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c9_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c10_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c10_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c11_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c11_dis_g = models.CharField(max_length=3, blank=True, null=True)
    c12_dis_b = models.CharField(max_length=3, blank=True, null=True)
    c12_dis_g = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_disable_enrolment_16_17'


class SchoolElevation3D(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    school_cod = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    own_distri = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    long = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    elevation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_elevation_3d'


class SchoolFacility1516(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    bldstatus = models.CharField(max_length=2, blank=True, null=True)
    clrooms = models.CharField(max_length=3, blank=True, null=True)
    clgood = models.CharField(max_length=3, blank=True, null=True)
    clmajor = models.CharField(max_length=2, blank=True, null=True)
    clminor = models.CharField(max_length=2, blank=True, null=True)
    toiletb = models.CharField(max_length=3, blank=True, null=True)
    toilet_g = models.CharField(max_length=3, blank=True, null=True)
    mealsinsch = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cal_yn = models.CharField(max_length=2, blank=True, null=True)
    hmroom_yn = models.CharField(max_length=2, blank=True, null=True)
    electric_yn = models.CharField(max_length=2, blank=True, null=True)
    bndrywall = models.CharField(max_length=2, blank=True, null=True)
    library_yn = models.CharField(max_length=2, blank=True, null=True)
    pground_yn = models.CharField(max_length=2, blank=True, null=True)
    bookinlib = models.CharField(max_length=6, blank=True, null=True)
    water = models.CharField(max_length=2, blank=True, null=True)
    medchk_yn = models.CharField(max_length=2, blank=True, null=True)
    ramps_yn = models.CharField(max_length=2, blank=True, null=True)
    computer = models.CharField(max_length=3, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'school_facility15_16'


class SchoolFacility1617(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    bldstatus = models.CharField(max_length=2, blank=True, null=True)
    clrooms = models.CharField(max_length=3, blank=True, null=True)
    clgood = models.CharField(max_length=3, blank=True, null=True)
    clmajor = models.CharField(max_length=2, blank=True, null=True)
    clminor = models.CharField(max_length=2, blank=True, null=True)
    toiletb = models.CharField(max_length=3, blank=True, null=True)
    toilet_g = models.CharField(max_length=3, blank=True, null=True)
    mealsinsch = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cal_yn = models.CharField(max_length=2, blank=True, null=True)
    hmroom_yn = models.CharField(max_length=2, blank=True, null=True)
    electric_yn = models.CharField(max_length=2, blank=True, null=True)
    bndrywall = models.CharField(max_length=2, blank=True, null=True)
    library_yn = models.CharField(max_length=2, blank=True, null=True)
    pground_yn = models.CharField(max_length=2, blank=True, null=True)
    bookinlib = models.CharField(max_length=6, blank=True, null=True)
    water = models.CharField(max_length=2, blank=True, null=True)
    medchk_yn = models.CharField(max_length=2, blank=True, null=True)
    ramps_yn = models.CharField(max_length=2, blank=True, null=True)
    computer = models.CharField(max_length=3, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'school_facility16_17'


class SchoolGeneral1516(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_afb_year = models.CharField(max_length=7, blank=True, null=True)
    rururb = models.CharField(max_length=2, blank=True, null=True)
    medinstr1 = models.CharField(max_length=3, blank=True, null=True)
    medinstr2 = models.CharField(max_length=3, blank=True, null=True)
    medinstr3 = models.CharField(max_length=3, blank=True, null=True)
    medinstr4 = models.CharField(max_length=3, blank=True, null=True)
    estdyear = models.CharField(max_length=4, blank=True, null=True)
    boardsec = models.CharField(max_length=2, blank=True, null=True)
    boardhsec = models.CharField(max_length=2, blank=True, null=True)
    ppsec_af8_yn = models.CharField(max_length=2, blank=True, null=True)
    schres_af8_yn = models.CharField(max_length=2, blank=True, null=True)
    schmgt = models.CharField(max_length=2, blank=True, null=True)
    lowclass = models.CharField(max_length=2, blank=True, null=True)
    highclass = models.CharField(max_length=2, blank=True, null=True)
    schcat = models.CharField(max_length=2, blank=True, null=True)
    ppstudent = models.CharField(max_length=5, blank=True, null=True)
    schtype = models.CharField(max_length=2, blank=True, null=True)
    schshi_af8_yn = models.CharField(max_length=2, blank=True, null=True)
    workdays_af8_pr = models.CharField(max_length=4, blank=True, null=True)
    workdays_af8_upr = models.CharField(max_length=4, blank=True, null=True)
    workdays_af8_sec = models.CharField(max_length=4, blank=True, null=True)
    workdays_af8_hsec = models.CharField(max_length=4, blank=True, null=True)
    noinspect = models.CharField(max_length=2, blank=True, null=True)
    resitype = models.CharField(max_length=2, blank=True, null=True)
    ppteacher = models.CharField(max_length=2, blank=True, null=True)
    visitsbrc = models.CharField(max_length=2, blank=True, null=True)
    visitscrc = models.CharField(max_length=2, blank=True, null=True)
    conti_af8_r = models.CharField(max_length=6, blank=True, null=True)
    conti_af8_e = models.CharField(max_length=6, blank=True, null=True)
    schmntcgrant_af8_r = models.CharField(max_length=6, blank=True, null=True)
    schmntcgrant_af8_e = models.CharField(max_length=6, blank=True, null=True)
    funds_af8_r = models.CharField(max_length=6, blank=True, null=True)
    funds_af8_e = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_general15_16'


class SchoolGeneral1617(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_afb_year = models.CharField(max_length=7, blank=True, null=True)
    rururb = models.CharField(max_length=2, blank=True, null=True)
    medinstr1 = models.CharField(max_length=3, blank=True, null=True)
    medinstr2 = models.CharField(max_length=3, blank=True, null=True)
    medinstr3 = models.CharField(max_length=3, blank=True, null=True)
    medinstr4 = models.CharField(max_length=3, blank=True, null=True)
    estdyear = models.CharField(max_length=4, blank=True, null=True)
    boardsec = models.CharField(max_length=2, blank=True, null=True)
    boardhsec = models.CharField(max_length=2, blank=True, null=True)
    ppsec_af8_yn = models.CharField(max_length=2, blank=True, null=True)
    schres_af8_yn = models.CharField(max_length=2, blank=True, null=True)
    schmgt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lowclass = models.CharField(max_length=2, blank=True, null=True)
    highclass = models.CharField(max_length=2, blank=True, null=True)
    schcat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ppstudent = models.CharField(max_length=5, blank=True, null=True)
    schtype = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    schshi_af8_yn = models.CharField(max_length=2, blank=True, null=True)
    workdays_af8_pr = models.CharField(max_length=4, blank=True, null=True)
    workdays_af8_upr = models.CharField(max_length=4, blank=True, null=True)
    workdays_af8_sec = models.CharField(max_length=4, blank=True, null=True)
    workdays_af8_hsec = models.CharField(max_length=4, blank=True, null=True)
    noinspect = models.CharField(max_length=2, blank=True, null=True)
    resitype = models.CharField(max_length=2, blank=True, null=True)
    ppteacher = models.CharField(max_length=2, blank=True, null=True)
    visitsbrc = models.CharField(max_length=2, blank=True, null=True)
    visitscrc = models.CharField(max_length=2, blank=True, null=True)
    conti_af8_r = models.CharField(max_length=6, blank=True, null=True)
    conti_af8_e = models.CharField(max_length=6, blank=True, null=True)
    schmntcgrant_af8_r = models.CharField(max_length=6, blank=True, null=True)
    schmntcgrant_af8_e = models.CharField(max_length=6, blank=True, null=True)
    funds_af8_r = models.CharField(max_length=6, blank=True, null=True)
    funds_af8_e = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_general16_17'


class SchoolObcenrolment1516(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    c1_ob = models.CharField(max_length=3, blank=True, null=True)
    c2_ob = models.CharField(max_length=3, blank=True, null=True)
    c3_ob = models.CharField(max_length=3, blank=True, null=True)
    c4_ob = models.CharField(max_length=3, blank=True, null=True)
    c5_ob = models.CharField(max_length=3, blank=True, null=True)
    c6_ob = models.CharField(max_length=3, blank=True, null=True)
    c7_ob = models.CharField(max_length=3, blank=True, null=True)
    c8_ob = models.CharField(max_length=3, blank=True, null=True)
    c9_ob = models.CharField(max_length=3, blank=True, null=True)
    c10_ob = models.CharField(max_length=3, blank=True, null=True)
    c11_ob = models.CharField(max_length=4, blank=True, null=True)
    c12_ob = models.CharField(max_length=3, blank=True, null=True)
    c1_og = models.CharField(max_length=3, blank=True, null=True)
    c2_og = models.CharField(max_length=3, blank=True, null=True)
    c3_og = models.CharField(max_length=3, blank=True, null=True)
    c4_og = models.CharField(max_length=3, blank=True, null=True)
    c5_og = models.CharField(max_length=3, blank=True, null=True)
    c6_og = models.CharField(max_length=3, blank=True, null=True)
    c7_og = models.CharField(max_length=3, blank=True, null=True)
    c8_og = models.CharField(max_length=3, blank=True, null=True)
    c9_og = models.CharField(max_length=3, blank=True, null=True)
    c10_og = models.CharField(max_length=3, blank=True, null=True)
    c11_og = models.CharField(max_length=3, blank=True, null=True)
    c12_og = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_obcenrolment15_16'


class SchoolObcenrolment1617(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    c1_ob = models.CharField(max_length=3, blank=True, null=True)
    c2_ob = models.CharField(max_length=3, blank=True, null=True)
    c3_ob = models.CharField(max_length=3, blank=True, null=True)
    c4_ob = models.CharField(max_length=3, blank=True, null=True)
    c5_ob = models.CharField(max_length=3, blank=True, null=True)
    c6_ob = models.CharField(max_length=3, blank=True, null=True)
    c7_ob = models.CharField(max_length=3, blank=True, null=True)
    c8_ob = models.CharField(max_length=3, blank=True, null=True)
    c9_ob = models.CharField(max_length=3, blank=True, null=True)
    c10_ob = models.CharField(max_length=3, blank=True, null=True)
    c11_ob = models.CharField(max_length=4, blank=True, null=True)
    c12_ob = models.CharField(max_length=3, blank=True, null=True)
    c1_og = models.CharField(max_length=3, blank=True, null=True)
    c2_og = models.CharField(max_length=3, blank=True, null=True)
    c3_og = models.CharField(max_length=3, blank=True, null=True)
    c4_og = models.CharField(max_length=3, blank=True, null=True)
    c5_og = models.CharField(max_length=3, blank=True, null=True)
    c6_og = models.CharField(max_length=3, blank=True, null=True)
    c7_og = models.CharField(max_length=3, blank=True, null=True)
    c8_og = models.CharField(max_length=3, blank=True, null=True)
    c9_og = models.CharField(max_length=3, blank=True, null=True)
    c10_og = models.CharField(max_length=3, blank=True, null=True)
    c11_og = models.CharField(max_length=3, blank=True, null=True)
    c12_og = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_obcenrolment16_17'


class SchoolRepeaters1516(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    fail1b = models.CharField(max_length=2, blank=True, null=True)
    fail2b = models.CharField(max_length=2, blank=True, null=True)
    fail3b = models.CharField(max_length=2, blank=True, null=True)
    fail4b = models.CharField(max_length=2, blank=True, null=True)
    fail5b = models.CharField(max_length=2, blank=True, null=True)
    fail6b = models.CharField(max_length=2, blank=True, null=True)
    fail7b = models.CharField(max_length=2, blank=True, null=True)
    fail8b = models.CharField(max_length=2, blank=True, null=True)
    fail9b = models.CharField(max_length=2, blank=True, null=True)
    fail10b = models.CharField(max_length=2, blank=True, null=True)
    fail11b = models.CharField(max_length=2, blank=True, null=True)
    fail12b = models.CharField(max_length=2, blank=True, null=True)
    fail1g = models.CharField(max_length=2, blank=True, null=True)
    fail2g = models.CharField(max_length=2, blank=True, null=True)
    fail3g = models.CharField(max_length=2, blank=True, null=True)
    fail4g = models.CharField(max_length=2, blank=True, null=True)
    fail5g = models.CharField(max_length=2, blank=True, null=True)
    fail6g = models.CharField(max_length=2, blank=True, null=True)
    fail7g = models.CharField(max_length=2, blank=True, null=True)
    fail8g = models.CharField(max_length=2, blank=True, null=True)
    fail9g = models.CharField(max_length=2, blank=True, null=True)
    fail10g = models.CharField(max_length=2, blank=True, null=True)
    fail11g = models.CharField(max_length=2, blank=True, null=True)
    fail12g = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_repeaters15_16'


class SchoolRepeaters1617(models.Model):
    schcd = models.CharField(max_length=11, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    fail1b = models.CharField(max_length=2, blank=True, null=True)
    fail2b = models.CharField(max_length=2, blank=True, null=True)
    fail3b = models.CharField(max_length=2, blank=True, null=True)
    fail4b = models.CharField(max_length=2, blank=True, null=True)
    fail5b = models.CharField(max_length=2, blank=True, null=True)
    fail6b = models.CharField(max_length=2, blank=True, null=True)
    fail7b = models.CharField(max_length=2, blank=True, null=True)
    fail8b = models.CharField(max_length=2, blank=True, null=True)
    fail9b = models.CharField(max_length=2, blank=True, null=True)
    fail10b = models.CharField(max_length=2, blank=True, null=True)
    fail11b = models.CharField(max_length=2, blank=True, null=True)
    fail12b = models.CharField(max_length=2, blank=True, null=True)
    fail1g = models.CharField(max_length=2, blank=True, null=True)
    fail2g = models.CharField(max_length=2, blank=True, null=True)
    fail3g = models.CharField(max_length=2, blank=True, null=True)
    fail4g = models.CharField(max_length=2, blank=True, null=True)
    fail5g = models.CharField(max_length=2, blank=True, null=True)
    fail6g = models.CharField(max_length=2, blank=True, null=True)
    fail7g = models.CharField(max_length=2, blank=True, null=True)
    fail8g = models.CharField(max_length=2, blank=True, null=True)
    fail9g = models.CharField(max_length=2, blank=True, null=True)
    fail10g = models.CharField(max_length=2, blank=True, null=True)
    fail11g = models.CharField(max_length=2, blank=True, null=True)
    fail12g = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_repeaters16_17'


class SchoolRte1617(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    workdays_pr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    workdays_upr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    schhrstch_pr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    schhrschild_upr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    schhrstch_upr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    approachbyroad = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cce_yn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr_maintained = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcr_shared = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wsec25p_enrolled = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smc_yn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smcmem_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smcmem_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smsparents_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smsparents_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smcnomlocal_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smcnomlocal_f = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smcmeetings = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smcsdp_yn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    smschildrec_yn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_cy_enrolled_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_cy_enrolled_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_cy_provided_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_cy_provided_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_py_enrolled_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_py_enrolled_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_py_provided_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_py_provided_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_by = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_place = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    spltrg_type = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    txtbkrecd_yn = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    txtbkmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    txtbkyear = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    acstartmnth = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mealsinsch = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kitshed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mdm_maintainer = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wsec25p_applied = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_rte16_17'


class SchoolScEnrolment1617(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    c1_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c2_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c3_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c4_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c5_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c6_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c7_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c8_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c9_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c10_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c11_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c12_cb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c1_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c2_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c3_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c4_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c5_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c6_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c7_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c8_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c9_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c10_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c11_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c12_cg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_sc_enrolment_16_17'


class SchoolStEnrolment1617(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    c1_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c2_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c3_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c4_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c5_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c6_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c7_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c8_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c9_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c10_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c11_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c12_tb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c1_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c2_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c3_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c4_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c5_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c6_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c7_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c8_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c9_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c10_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c11_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c12_tg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_st_enrolment_16_17'


class SchoolTeachers1617(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    tch_male = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tch_female = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tch_nr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    headtch = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    htchname = models.CharField(max_length=50, blank=True, null=True)
    gradabove = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tchwithprof = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    daysinvld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tchinvld = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_teachers_16_17'


class SchoolTotalEnrolment1617(models.Model):
    schcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac_year = models.CharField(max_length=7, blank=True, null=True)
    c1_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c1_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c2_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c2_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c3_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c3_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c4_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c4_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c5_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c5_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c6_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c6_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c7_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c7_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c8_totb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c8_totg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c9_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c9_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c10_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c10_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c11_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c11_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c12_b = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c12_g = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    senrb5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    senrg5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    senrb8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    senrg8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    apprb5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    apprg5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    apprb8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    apprg8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    passb5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    passg5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    passb8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    passg8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p60b5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p60g5 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p60b8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    p60g8 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_total_enrolment16_17'


class SchoolTypeMgntBuilding(models.Model):
    distname = models.CharField(max_length=100, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)
    village_name = models.CharField(max_length=100, blank=True, null=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    schtype = models.CharField(max_length=100, blank=True, null=True)
    bldstatus = models.CharField(max_length=100, blank=True, null=True)
    schmgnt = models.CharField(max_length=100, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    typstatusngntid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_type_mgnt_building'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Taluka(models.Model):
    s_no = models.CharField(max_length=2, blank=True, null=True)
    district_code = models.CharField(max_length=30, blank=True, null=True)
    district_name_in_english = models.CharField(max_length=30, blank=True, null=True)
    district_name_in_local_language = models.CharField(max_length=30, blank=True, null=True)
    hierarchy = models.CharField(max_length=30, blank=True, null=True)
    short_name_of_district = models.CharField(max_length=30, blank=True, null=True)
    census_2001_code = models.CharField(max_length=30, blank=True, null=True)
    census2011_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taluka'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=20)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'


class UrcMatchingBlocknames(models.Model):
    block_name1 = models.CharField(max_length=100, blank=True, null=True)
    pincode1 = models.CharField(max_length=6, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urc_matching_blocknames'


class UrcMatchingBlocknames1(models.Model):
    block_name1 = models.CharField(max_length=100, blank=True, null=True)
    pincode1 = models.CharField(max_length=6, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    block_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urc_matching_blocknames1'


class VillageNameCompareLgCensus(models.Model):
    vid = models.IntegerField(primary_key=True)
    village_code = models.IntegerField(blank=True, null=True)
    vcensus_2011code = models.IntegerField(blank=True, null=True)
    lg_distname = models.CharField(max_length=20, blank=True, null=True)
    district_code_2017 = models.IntegerField(blank=True, null=True)
    district_name_2017 = models.CharField(max_length=20, blank=True, null=True)
    district_name_matches = models.CharField(max_length=20, blank=True, null=True)
    subdistrict_code = models.IntegerField(blank=True, null=True)
    taluka_code2011 = models.IntegerField(blank=True, null=True)
    subdistrict_name = models.CharField(max_length=20, blank=True, null=True)
    taluka_name = models.CharField(max_length=20, blank=True, null=True)
    taluka_name_matches = models.CharField(max_length=20, blank=True, null=True)
    lg_villagename = models.CharField(max_length=20, blank=True, null=True)
    census11_villagename = models.CharField(max_length=20, blank=True, null=True)
    village_name_matches = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village_name_compare_lg_census'
