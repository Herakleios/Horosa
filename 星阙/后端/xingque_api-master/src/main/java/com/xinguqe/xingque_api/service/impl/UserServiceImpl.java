package com.xinguqe.xingque_api.service.impl;

import com.github.pagehelper.PageHelper;
import com.xinguqe.xingque_api.dto.BO.WechatAccessTokenBO;
import com.xinguqe.xingque_api.dto.BO.WechatUserBO;
import com.xinguqe.xingque_api.dto.admin.response.PageDataRsp;
import com.xinguqe.xingque_api.dto.admin.request.PageVO;
import com.xinguqe.xingque_api.dto.request.*;
import com.xinguqe.xingque_api.entity.*;
import com.xinguqe.xingque_api.exception.HorosaException;
import com.xinguqe.xingque_api.mapper.UserBehaviorMapper;
import com.xinguqe.xingque_api.mapper.UserConfigMapper;
import com.xinguqe.xingque_api.mapper.UserMapper;
import com.xinguqe.xingque_api.mapper.UserSuggestMapper;
import com.xinguqe.xingque_api.service.UserService;
import com.xinguqe.xingque_api.utils.md5.Md5Utils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.List;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserConfigMapper userConfigMapper;

    @Autowired
    private UserMapper userMapper;

    @Autowired
    private UserSuggestMapper userSuggestMapper;

    @Autowired
    private UserBehaviorMapper userBehaviorMapper;

    public User login(UserLoginVO userLoginVO) throws HorosaException {
        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andUserNameEqualTo(userLoginVO.username).andStatusEqualTo(1);
        User user = userMapper.selectFirstByExample(userExample);

        if (user == null) {
            throw new  HorosaException(1002,"用户名或密码错误");
        }
        String pwd = Md5Utils.encryptMD5(userLoginVO.password + user.getSalt());
        if (!user.getPassword().equals(pwd)) {
            throw new  HorosaException(1002,"用户名或密码错误");
        }

        return user;
    }

    ;

    public User info(int userId) {
        return userMapper.selectByPrimaryKey(userId);
    }

    public int modifyInfo(UserVO userVO,int userId) {
        User user = new User();
        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andIdEqualTo(userId);

        user.setAvatar(userVO.avatar);
        user.setName(userVO.name);
        user.setSex(userVO.sex);
        user.setBirthday(userVO.birthday);
        user.setResidenceProvinceId(userVO.residenceProvinceId);
        user.setResidenceCityId(userVO.residenceCityId);
        user.setResidenceDistrictId(userVO.residenceDistrictId);
        user.setBirthProvinceId(userVO.birthProvinceId);
        user.setBirthCityId(userVO.birthCityId);
        user.setBirthDistrictId(userVO.birthDistrictId);

        return userMapper.updateByExampleSelective(user,userExample);
    }


    public User AddOrUpdateUser(WechatAccessTokenBO accessToken, WechatUserBO wechatUser){
        //根据用户信息查询是否存在
        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andWxOpenidEqualTo(accessToken.openid).andWxUnionidEqualTo(accessToken.unionid).andStatusEqualTo(1);

        User user = userMapper.selectFirstByExample(userExample);
        if (user == null || user.getId() <= 0) {
            //新增用户
            user = new User();
            user.setAvatar(wechatUser.headimgurl);
            user.setName(wechatUser.nickname);
            user.setWxOpenid(accessToken.openid);
            user.setWxUnionid(accessToken.unionid);
            user.setStatus(1);
            int id = userMapper.insertSelective(user);
            user.setId(user.getId());
        }

        return user;
    }

    @Override
    public UserConfig getConfig(int userId) {
        UserConfigExample userConfigExample = new UserConfigExample();
        UserConfigExample.Criteria criteria =  userConfigExample.createCriteria();
        criteria.andUserIdEqualTo(userId).andStatusEqualTo(1);

        return userConfigMapper.selectFirstByExample(userConfigExample);
    }

    @Override
    public int setConfig(UserConfigVO userConfigVO,int userId) {
        UserConfig userConfig = new UserConfig();
        userConfig.setUserId(userId);
        userConfig.setApparentSolarTime(userConfigVO.apparentSolarTime);
        userConfig.setQimenType(userConfigVO.qimenType);
        userConfig.setLiurenType(userConfigVO.liurenType);
        //todo 八字连线设置

        return userConfigMapper.insert(userConfig);
    }

    public int suggest(SuggestVO suggest, int userId) {
        UserSuggest userSuggest = new UserSuggest();

        userSuggest.setUserId(userId);
        userSuggest.setContent(suggest.content);
        userSuggest.setImages(suggest.images);

        return userSuggestMapper.insertSelective(userSuggest);
    }

    public int addBehavior(UserBehaviorVO data,int userId) {
        UserBehavior userBehavior = new UserBehavior();
        userBehavior.setUserId(userId);
        userBehavior.setModule(data.module);
        userBehavior.setOperate(data.operate);
        userBehavior.setStatus(1);
        return userBehaviorMapper.insertSelective(userBehavior);
    }

    public PageDataRsp<List<User>> listByAdd(PageVO pageVO) {
        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andStatusEqualTo(1);

        long count = userMapper.countByExample(userExample);

        PageHelper.startPage(pageVO.page, pageVO.pageSize);
        List<User> list = userMapper.selectByExample(userExample);

        PageDataRsp<List<User>> data = new PageDataRsp<>();
        data.setData(list);
        data.setTotal(count);
        return data;
    }

    public int register(UserRegisterVO userRegisterVO) throws HorosaException {
        User user = new User();

        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andUserNameEqualTo(userRegisterVO.username).andStatusEqualTo(1);
        User userExist = userMapper.selectFirstByExample(userExample);

        if (userExist != null) {
            throw new HorosaException(1003,"用户已存在");
        }


        SecureRandom secureRandom = new SecureRandom();
        BigInteger bigInteger = new BigInteger(30, secureRandom);
        String salt = bigInteger.toString().substring(0,6);

        String password = Md5Utils.encryptMD5(userRegisterVO.password + salt);

        user.setName(userRegisterVO.username);
        user.setUserName(userRegisterVO.username);
        user.setPassword(password);
        user.setSalt(salt);

        userMapper.insertSelective(user);
        return user.getId();
    }

    public int Del(UserDelVO userDelVO){
        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andIdEqualTo(userDelVO.userId);

        return userMapper.deleteByExample(userExample);
    }
}
