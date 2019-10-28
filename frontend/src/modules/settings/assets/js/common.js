function get_netbios_domain(domain) {
	if (!domain.includes(".")) {
		return domain.toUpperCase()
	} else if (domain.includes(".")) {
		let prefix = domain.split(".")[0];
		return prefix.toUpperCase()
	}
}

export { get_netbios_domain };