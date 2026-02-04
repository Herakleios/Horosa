import 'package:flutter/material.dart';
import 'package:fluwx/fluwx.dart';
import 'package:horosa/app.dart';
import 'package:horosa/utils/copy_database.dart';
import 'package:horosa/widgets/chn_place_picker.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  Fluwx fluwx = Fluwx();
  fluwx.registerApi(
    appId: 'wx8559b476b39e28d1',
    universalLink: 'https://mobileweb.horosa.com/app/',
  );
  await copyDatabase();
  await CHNPlaceLoader.instance.loadRegions();
  runApp(const HorosaApp());
}
