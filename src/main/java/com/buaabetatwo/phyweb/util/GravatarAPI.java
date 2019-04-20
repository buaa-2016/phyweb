package com.buaabetatwo.phyweb.util;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

public class GravatarAPI {
    private static HashMap<String, String> cache = new HashMap<>();

    public static String emailToAvatarUrl(String email) {
        if (cache.containsKey(email)) {
            return cache.get(email);
        }
        String md5 = hexmd5(email);
        String avatarUrl = "http://www.gravatar.com/avatar/" + md5 +
                "?s=200&default=https%3A%2F%2Fws1.sinaimg.cn%2Fmw690%2F0070O95Yly1g29icq3u7oj30xc0xc4dj.jpg";
        cache.put(email, avatarUrl);
        return avatarUrl;
    }

    private static String hexmd5(String str) {
        StringBuffer hexString = new StringBuffer();
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        byte[] hash = md.digest(str.getBytes());

        for (int i = 0; i < hash.length; i++) {
            if ((0xff & hash[i]) < 0x10) {
                hexString.append("0"
                        + Integer.toHexString((0xFF & hash[i])));
            } else {
                hexString.append(Integer.toHexString(0xFF & hash[i]));
            }
        }
        return hexString.toString();
    }

}
