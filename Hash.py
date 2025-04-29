def hash_password(password):
    import hashlib
    hash_algo = hashlib.new("SHA256")
    hash_algo.update(password.encode())
    hashed_password = hash_algo.hexdigest()
    print(hashed_password)
    return hashed_password


