import 'package:dio/dio.dart';
import 'package:horosa/models/user_info.dart';
import 'package:horosa/utils/http.dart';

class ProfileSvc {
  static HTTPUtil httpUtil = HTTPUtil();

  /// 注册账号
  static Future<Response> register(String username, String password, String confirmPassword) async {
    final response = await httpUtil.post(
      '/user/register',
      useCache: false,
      useAuth: false,
      data: {
        'username': username,
        'password': password,
        'confirm_password': confirmPassword
      }
    );

    return response;
  }

  /// 账号登录
  static Future<Response> login(String username, String password) async {
    final response = await httpUtil.post(
      '/user/login',
      useCache: false,
      useAuth: false,
      data: {
        'username': username,
        'password': password
      }
    );

    return response;
  }

  /// 获取用户信息
  static Future<Response> getUserInfo() async {
    final response = await httpUtil.post(
      '/user/info',
      useCache: false,
    );

    return response;
  }

  /// 修改用户信息
  static Future<Response> updateUserInfo(UserInfo userInfo) async {
    final response = await httpUtil.post(
      '/user/modify',
      useCache: false,
      data: userInfo.toJson()
    );

    return response;
  }

  /// 注销用户
  static Future<Response> deregister() async {
    final response = await httpUtil.post(
        'cancel_user',
        useCache: false,
    );

    return response;
  }

  /// 获取起卦列表
  static Future<Response>  getRelationBook({int page = 1, int size = 10}) async {
    final response = await httpUtil.post(
        '/trigram_book/list',
        useCache: false,
        data: {
          'page': page,
          'page_size': size,
        });

    return response;
  }

  /// 创建起卦人
  static Future<Response> createRelation(Relation relation) async {
    final response = await httpUtil.post(
        '/trigram_book/add',
        useCache: false,
        data: relation.toJson()
    );

    return response;
  }

  /// 修改起卦人
  static Future<Response> updateRelation(Relation relation) async {
    final response = await httpUtil.post(
        '/trigram_book/modify',
        useCache: false,
        data: relation.toJson()
    );

    return response;
  }

  /// 删除起卦人
  static Future<Response> removeRelation(int id) async {
    final response = await httpUtil.post(
        '/trigram_book/del?id=$id',
        useCache: false,
        data: {'id': id}
    );

    return response;
  }
}
