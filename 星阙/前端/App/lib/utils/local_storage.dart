import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class LocalStorage {
  // 私有构造函数
  LocalStorage._privateConstructor();

  // 唯一实例
  static final LocalStorage _instance = LocalStorage._privateConstructor();

  // 工厂构造函数，返回唯一实例
  factory LocalStorage() {
    return _instance;
  }

  final FlutterSecureStorage _storage = const FlutterSecureStorage();

  // 存储数据
  Future<void> write(String key, String value) async {
    await _storage.write(key: key, value: value);
  }

  // 读取数据
  Future<String?> read(String key) async {
    return await _storage.read(key: key);
  }

  // 删除数据
  Future<void> delete(String key) async {
    await _storage.delete(key: key);
  }

  // 清除所有数据
  Future<void> deleteAll() async {
    await _storage.deleteAll();
  }
}
