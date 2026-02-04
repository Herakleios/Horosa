import 'package:flutter/widgets.dart';
import 'package:horosa/models/user_info.dart';
import 'package:horosa/services/profile.dart';
import 'package:horosa/utils/local_storage.dart';
import 'package:horosa/constants/keys.dart';

LocalStorage _localStorage = LocalStorage();

class AuthProvider extends ChangeNotifier {
  // 是否需要提示用户登录
  bool needRemind = true;

  String? token;
  UserInfo? userInfo;

  bool get isLoggedIn => token != null && userInfo != null;

  AuthProvider() {
    _loadTokenFromStorage();
  }

  Future<void> _loadTokenFromStorage() async {
    String? token = await _localStorage.read(AppKeys.accessToken);
    if(token != null) {
      setToken(token);
    }
    if(token != null && userInfo == null) {
      ProfileSvc.getUserInfo().then((res) {
        if(res.data['code'] == 10401) {
          _localStorage.delete(AppKeys.accessToken);
          setToken(null);
          setUserInfo(null);
          return;
        }
        if(res.data['code'] == 0) {
          setUserInfo(UserInfo.fromJson(res.data['data'] as Map<String, dynamic>));
        }
      });
    }
    notifyListeners();
  }

  void setToken(String? newToken) {
    token = newToken;
    notifyListeners();
  }

  void setUserInfo(UserInfo? newUserInfo) {
    userInfo = newUserInfo;
    notifyListeners();
  }

  void setNeedRemind(bool newNeedRemind) {
    needRemind = newNeedRemind;
    notifyListeners();
  }
}