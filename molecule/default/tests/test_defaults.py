import pytest

def get_home_dir(host):
    return host.check_output("printf %s \"$HOME\"").strip()

def test_mcw_resource_pack_dir(host):

    mcw_resource_pack_dir = host.file(f'{get_home_dir(host)}/.minecraft/resourcepacks/Waterland')
    assert mcw_resource_pack_dir.exists
    assert mcw_resource_pack_dir.is_directory
    assert mcw_resource_pack_dir.mode == 0o755

def test_mcw_resource_pack_assets_dir(host):

    mcw_resource_pack_assets_dir = host.file(f'{get_home_dir(host)}/.minecraft/resourcepacks/Waterland/assets')
    assert mcw_resource_pack_assets_dir.exists
    assert mcw_resource_pack_assets_dir.is_directory
    assert mcw_resource_pack_assets_dir.mode == 0o755

def test_mcw_resource_pack_meta_file(host):

    mcw_resource_pack_meta_file = host.file(f'{get_home_dir(host)}/.minecraft/resourcepacks/Waterland/pack.mcmeta')
    assert mcw_resource_pack_meta_file.exists
    assert mcw_resource_pack_meta_file.is_file
    assert mcw_resource_pack_meta_file.mode == 0o644

def test_mcw_resource_pack_icon_file(host):

    mcw_resource_pack_icon_file = host.file(f'{get_home_dir(host)}/.minecraft/resourcepacks/Waterland/pack.png')
    assert mcw_resource_pack_icon_file.exists
    assert mcw_resource_pack_icon_file.is_file
    assert mcw_resource_pack_icon_file.mode == 0o644

def test_mcw_resource_pack_entity_player_slim_dir(host):

    mcw_resource_pack_entity_player_slim_dir = host.file(f'{get_home_dir(host)}/.minecraft/resourcepacks/Waterland/assets/minecraft/textures/entity/player/slim')
    assert mcw_resource_pack_entity_player_slim_dir.exists
    assert mcw_resource_pack_entity_player_slim_dir.is_directory
    assert mcw_resource_pack_entity_player_slim_dir.mode == 0o755

def test_mcw_resource_pack_entity_player_wide_dir(host):

    mcw_resource_pack_entity_player_wide_dir = host.file(f'{get_home_dir(host)}/.minecraft/resourcepacks/Waterland/assets/minecraft/textures/entity/player/wide')
    assert mcw_resource_pack_entity_player_wide_dir.exists
    assert mcw_resource_pack_entity_player_wide_dir.is_directory
    assert mcw_resource_pack_entity_player_wide_dir.mode == 0o755
