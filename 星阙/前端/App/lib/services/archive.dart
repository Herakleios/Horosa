import 'package:dio/dio.dart';
import 'package:horosa/models/archive.dart';
import 'package:horosa/utils/http.dart';

class ArchiveSvc {
  static HTTPUtil httpUtil = HTTPUtil();

  static Future<Response> getArchiveList({int page = 1, int size = 10}) async {
    final response = await httpUtil.post(
        baseUrl: 'https://api.horosa.com',
        '/trigram/record_list',
        useCache: false,
        data: {
          'page': page,
          'page_size': size,
        });

    return response;
  }

  static Future<Response> removeArchive(int id) async {
    final response = await httpUtil.post(
        '/trigram/del_record',
        useCache: false,
        data: {
          'id': id,
        }
    );

    return response;
  }

  /// 添加记录 | 修改记录 type 1八字 2 六爻 3 六壬 4 奇门
  static Future<Response> record(ArchiveItem item) async {
    final response = await httpUtil.post(
        '/trigram/add_record',
        useCache: false,
        data: item.toJson()
    );

    return response;
  }
}
