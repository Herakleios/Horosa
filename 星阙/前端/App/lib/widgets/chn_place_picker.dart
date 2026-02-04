import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:horosa/models/chn_region.dart';
import 'package:horosa/models/picker.dart';
import 'package:horosa/widgets/forms/forms.dart';

class CHNPlaceAdcode {
  final int province;
  final int city;
  final int county;

  const CHNPlaceAdcode({
    required this.province,
    required this.city,
    required this.county,
  });

  @override
  String toString() {
    return '$province-$city-$county';
  }
}

class CHNPlace {
  final String province;
  final String city;
  final String county;
  final CHNPlaceAdcode adcode;
  final double lat;
  final double lng;

  const CHNPlace({
    required this.province,
    required this.city,
    required this.county,
    required this.adcode,
    required this.lat,
    required this.lng,
  });

  static CHNPlace fromAdcode(CHNPlaceAdcode? adcode) {
    // 验证 adcode 是否有效
    if (adcode == null || adcode.province == 0 || adcode.city == 0 || adcode.county == 0) {
      return CHNPlaceLoader.instance.getPlaceFromAdcode(const CHNPlaceAdcode(
        province: 99000000,
        city: 99010000,
        county: 99010100,
      ));
    }
    return CHNPlaceLoader.instance.getPlaceFromAdcode(adcode);
  }

  String toFullString() {
    return '$province-$city-$county';
  }

  @override
  String toString() {
    return '$city-$county';
  }
}

class CHNPlaceLoader {
  List<CHNRegion>? _regions;

  CHNPlaceLoader._internal();

  static final CHNPlaceLoader instance = CHNPlaceLoader._internal();

  Future<void> loadRegions() async {
    if (_regions == null) {
      final String response =
          await rootBundle.loadString('assets/database/regions.json');
      List<int> bytes = utf8.encode(response);
      List<int> compressed = gzip.encode(bytes);
      List<int> decompressed = gzip.decode(compressed);
      final List<dynamic> data = json.decode(utf8.decode(decompressed));
      _regions = data.map((e) => CHNRegion.fromJson(e)).toList();
    }
  }

  CHNPlace getPlaceFromAdcode(CHNPlaceAdcode adcode) {
    if (_regions == null) {
      throw Exception('Regions data has not been loaded.');
    }

    try {
      // 验证 adcode 是否有效
      if (adcode.province == 0 || adcode.city == 0 || adcode.county == 0) {
        return getPlaceFromAdcode(const CHNPlaceAdcode(
          province: 99000000,
          city: 99010000,
          county: 99010100,
        ));
      }
      CHNRegion province = _regions!.firstWhere(
          (province) => province.adcode == adcode.province,
          orElse: () =>
              throw StateError('No province found for adcode: $adcode'));
      CHNRegion city = province.children.firstWhere(
          (city) => city.adcode == adcode.city,
          orElse: () => throw StateError('No city found for adcode: $adcode'));
      CHNRegion county = city.children.firstWhere(
          (district) => district.adcode == adcode.county,
          orElse: () =>
              throw StateError('No county found for adcode: $adcode'));

      return CHNPlace(
        province: province.name,
        city: city.name,
        county: county.name,
        adcode: adcode,
        lat: county.lat,
        lng: county.lng,
      );
    } catch (e) {
      throw StateError('Error processing adcode: $adcode - ${e.toString()}');
    }
  }
}

class CHNPlacePicker extends StatefulWidget {
  const CHNPlacePicker({super.key, this.value, this.onChange});

  final CHNPlace? value;
  final Function(CHNPlace)? onChange;

  @override
  State<CHNPlacePicker> createState() => _CHNPlacePickerState();
}

class _CHNPlacePickerState extends State<CHNPlacePicker> {
  bool loading = true;

  late int provinceId;
  late int cityId;
  late int countyId;

  List<CHNRegion> provinces = [];
  List<CHNRegion> cities = [];
  List<CHNRegion> counties = [];

  late FixedExtentScrollController provinceController,
      cityController,
      countyController;

  List<CHNRegion> getCities() =>
      provinces.firstWhere((region) => region.adcode == provinceId).children;

  List<CHNRegion> getCounties() => provinces
      .firstWhere((region) => region.adcode == provinceId)
      .children
      .firstWhere((region) => region.adcode == cityId)
      .children;

  Future<void> loadRegionData() async {
    final String response =
        await rootBundle.loadString('assets/database/regions.json');
    List<int> bytes = utf8.encode(response);
    List<int> compressed = gzip.encode(bytes);
    List<int> decompressed = gzip.decode(compressed);
    final List<dynamic> data = json.decode(utf8.decode(decompressed));
    List<CHNRegion> regions = data.map((e) => CHNRegion.fromJson(e)).toList();

    setState(() {
      provinces = regions;
      provinceId = widget.value != null
          ? widget.value!.adcode.province
          : provinces.first.adcode;
      cities = getCities();
      cityId = widget.value != null
          ? widget.value!.adcode.city
          : cities.first.adcode;
      counties = getCounties();
      countyId =
          widget.value != null ? widget.value!.adcode .county: counties.first.adcode;
      loading = false;
    });
    widget.onChange?.call(CHNPlace(
        province:
            provinces.firstWhere((region) => region.adcode == provinceId).name,
        city: cities.firstWhere((region) => region.adcode == cityId).name,
        county: counties.firstWhere((region) => region.adcode == countyId).name,
        adcode: CHNPlaceAdcode(
          province: provinceId,
          city: cityId,
          county: countyId,
        ),
        lat: counties.first.lat,
        lng: counties.first.lng));
  }

  @override
  void initState() {
    super.initState();
    loadRegionData().then((_) {
      provinceController = FixedExtentScrollController(
          initialItem:
              provinces.indexWhere((region) => region.adcode == provinceId));
      cityController = FixedExtentScrollController(
          initialItem: cities.indexWhere((region) => region.adcode == cityId));
      countyController = FixedExtentScrollController(
          initialItem:
              counties.indexWhere((region) => region.adcode == countyId));
    });
  }

  @override
  void dispose() {
    provinceController.dispose();
    cityController.dispose();
    countyController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return loading
        ? const Center(child: CircularProgressIndicator())
        : Row(
            children: [
              Expanded(
                child: HorosaPicker(
                  controller: provinceController,
                  options: provinces,
                  value: provinceId,
                  mapper: (region) => PickerItem(
                    label: region.name,
                    value: region.adcode,
                  ),
                  onChange: (region, item) {
                    setState(() {
                      provinceId = item.value;
                      cities = region.children;
                      cityId = cities.first.adcode;
                      counties = getCounties();
                      countyId = counties.first.adcode;

                      cityController.jumpToItem(cities
                          .indexWhere((region) => region.adcode == cityId));
                      countyController.jumpToItem(counties
                          .indexWhere((region) => region.adcode == countyId));

                      widget.onChange?.call(CHNPlace(
                        province: region.name,
                        city: cities.first.name,
                        county: counties.first.name,
                        adcode: CHNPlaceAdcode(
                          province: region.adcode,
                          city: cities.first.adcode,
                          county: counties.first.adcode,
                        ),
                        lat: counties.first.lat,
                        lng: counties.first.lng,
                      ));
                    });
                  },
                ),
              ),
              Expanded(
                child: HorosaPicker(
                  controller: cityController,
                  options: cities,
                  value: cityId,
                  mapper: (region) => PickerItem(
                    label: region.name,
                    value: region.adcode,
                  ),
                  onChange: (region, item) {
                    setState(() {
                      cityId = item.value;
                      counties = region.children;
                      countyId = counties.first.adcode;

                      countyController.jumpToItem(counties
                          .indexWhere((region) => region.adcode == countyId));
                      widget.onChange?.call(CHNPlace(
                        province: provinces
                            .firstWhere((r) => r.adcode == provinceId)
                            .name,
                        city: region.name,
                        county: counties.first.name,
                        adcode: CHNPlaceAdcode(
                          province: provinceId,
                          city: region.adcode,
                          county: counties.first.adcode
                        ),
                        lat: counties.first.lat,
                        lng: counties.first.lng,
                      ));
                    });
                  },
                ),
              ),
              Expanded(
                child: HorosaPicker(
                  controller: countyController,
                  options: counties,
                  value: countyId,
                  mapper: (region) => PickerItem(
                    label: region.name,
                    value: region.adcode,
                  ),
                  onChange: (region, item) {
                    setState(() {
                      countyId = item.value;
                      widget.onChange?.call(CHNPlace(
                        province: provinces
                            .firstWhere((r) => r.adcode == provinceId)
                            .name,
                        city: cities.firstWhere((r) => r.adcode == cityId).name,
                        county: region.name,
                        adcode: CHNPlaceAdcode(
                          province: provinceId,
                          city: cityId,
                          county: region.adcode,
                        ),
                        lat: region.lat,
                        lng: region.lng,
                      ));
                    });
                  },
                ),
              ),
            ],
          );
  }
}
