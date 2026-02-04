package com.xinguqe.xingque_api.service;

import com.xinguqe.xingque_api.dto.admin.request.QuickLinkVO;
import com.xinguqe.xingque_api.entity.QuickLink;

import java.util.List;

public interface QuickLinkService {
    List<QuickLink> quickLinkList();
    int modify(QuickLinkVO quickLinkVO);
}
