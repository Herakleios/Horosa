import 'package:dio/dio.dart';
import 'package:horosa/utils/http.dart';

class FeedbackSvc {
  static HTTPUtil httpUtil = HTTPUtil();

  /// 意见反馈
  static Future<Response> feedback(String content) async {
    final response = await httpUtil.post(
      '/user/suggest',
      useCache: false,
      data: {
        'content': content
      }
    );

    return response;
  }
}